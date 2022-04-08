
#El objetivo de este proyecto es analizar si hay una relacion entre las criptomonedas mas
#importantes en el mercado y si es posible modelar una tendencia a una de estas por regresion polinomial. 
#Para ello, se obtuvieron datos por la funcion de excel STOCKHISTORY que provee informacion de los precios de las criptomonedas mas
#importantes con respecto al tiempo, proveidos por Microsoft. Se uso un rango de aproximadamente 2 años 
#(principio de 2019) hasta ahora. Hay que tener en cuenta que una de las monedas (XRP) estuvo disponible recien
#en marzo de 2019.



library(readxl);library(openxlsx);library(dplyr);library(ggplot2);library(caTools);library(dendextend);library(cluster)
setwd("C:\\Users\\Francisco\\Desktop")
Tabla_datos=read_excel("DatosCripto.xlsx")
Tabla_datos=Tabla_datos[-1,]
Tabla_datos=as.data.frame(Tabla_datos)

#Cambio el nombre de las columnas
colnames(Tabla_datos)=c("BTC/Fecha","BTC/Precio","ETH/Fecha","ETH/Precio","XRP/Fecha","XRP/Precio","LTC/Fecha","LTC/Precio","BCH/Fecha","BCH/Precio")

#Convierto los precios a formato numero
Tabla_datos$`BTC/Precio`=as.numeric(Tabla_datos$`BTC/Precio`)
Tabla_datos$`ETH/Precio`=as.numeric(Tabla_datos$`ETH/Precio`)
Tabla_datos$`XRP/Precio`=as.numeric(Tabla_datos$`XRP/Precio`)
Tabla_datos$`LTC/Precio`=as.numeric(Tabla_datos$`LTC/Precio`)
Tabla_datos$`BCH/Precio`=as.numeric(Tabla_datos$`BCH/Precio`)

#Para armar el data frame, hay que hacer que dependan los precios de las monedas a una variable, las fechas.
#Para ello, se agrega una columna con todas las fechas de compra de las monedas, se ordenan y se eliminan las repetidas.
#Se hace esto ya que en la base de datos faltan algunos dias con sus valores.
Fechas=c(Tabla_datos$`BTC/Fecha`,Tabla_datos$`ETH/Fecha`,Tabla_datos$`XRP/Fecha`,Tabla_datos$`LTC/Fecha`,Tabla_datos$`BCH/Fecha`)
Fechas=unique(sort(Fechas))
Tabla_datos=Tabla_datos
Tabla_datos$Fechas=Fechas

#Se arma una funcion donde poniendo como argumentos las fechas de precio de moneda, el precio en si y la
#fecha total, devuelva un vector donde esta el precio de moneda cuando coincide una fecha o un NA cuando
#no se encontro la fecha.

def1=function(Fechamon,Preciomon,Fechas){
  j=1
  col=c()
  for (i in 1:length(Fechas)){
    if(is.na(Fechamon[j])){
      break
    }
    else{
      if (Fechas[i]==Fechamon[j]){
        col=c(col,Preciomon[j])
        j=j+1
      }
      else{
        col=c(col,NA)
      }
    }
  }
  return(col)
}

#Se aplica la funcion a los precios, y se eliminan las fechas ya que tenemos todas las columnas coincidentes
#con la columna unica de fechas.

Tabla_datos$`BTC/Precio`=def1(Tabla_datos$`BTC/Fecha`,Tabla_datos$`BTC/Precio`,Tabla_datos$Fechas)
Tabla_datos$`ETH/Precio`=def1(Tabla_datos$`ETH/Fecha`,Tabla_datos$`ETH/Precio`,Tabla_datos$Fechas)
Tabla_datos$`XRP/Precio`=def1(Tabla_datos$`XRP/Fecha`,Tabla_datos$`XRP/Precio`,Tabla_datos$Fechas)
Tabla_datos$`LTC/Precio`=def1(Tabla_datos$`LTC/Fecha`,Tabla_datos$`LTC/Precio`,Tabla_datos$Fechas)
Tabla_datos$`BCH/Precio`=def1(Tabla_datos$`BCH/Fecha`,Tabla_datos$`BCH/Precio`,Tabla_datos$Fechas)
Tabla_datos$`BTC/Fecha`=NULL
Tabla_datos$`ETH/Fecha`=NULL
Tabla_datos$`XRP/Fecha`=NULL
Tabla_datos$`LTC/Fecha`=NULL
Tabla_datos$`BCH/Fecha`=NULL

#Convierto las fechas a tipo Date y la muevo al principio. Omito de la tabla las filas con NA, no servirian para comparar.
Tabla_datos$Fechas=convertToDate(Tabla_datos$Fechas)
Tabla_datos=Tabla_datos[,c(6,1,2,3,4,5)]
Tabla_datos=na.omit(Tabla_datos)

#Preparo un dataframe para representar en un solo grafico los valores de las monedas con respecto al tiempo.
vec=c(Tabla_datos$`BTC/Precio`,Tabla_datos$`ETH/Precio`,Tabla_datos$`XRP/Precio`,Tabla_datos$`LTC/Precio`,Tabla_datos$`BCH/Precio`)
Graf=data.frame(Tabla_datos$Fechas,vec,factor(rep(c("BTC","ETH","XRP","LTC","BCH"),each=length(Tabla_datos$Fechas))))
colnames(Graf)=c("Fechas","Valor","Criptomoneda")
ggplot(Graf,aes(x=`Fechas`,y=`Valor`,color=`Criptomoneda`))+geom_point(size=0.5)+scale_y_log10()+ggtitle("Tendencia criptomonedas vs tiempo")+stat_smooth()

#En el grafico se ve que los valores de Bitcoin y Ethereum se relacionan bastante entre si. 
#Confirmo usando cor()

cor(Tabla_datos$`BTC/Precio`,Tabla_datos$`ETH/Precio`)

#El valor es bastante alto, buena correlacion.


#Relaciono entre los distintos tipos de monedas por clustering, normalizando para comparar. 
#A travez del dendograma, podemos ver que se confirma
#la relacion entre Bitcoin y Ethereum, mientras que Litecoin y Bitcoin Cash tienen una buena correlacion.


normalize = function(x) { 
  num = x - min(x) 
  denom = max(x) - min(x) 
  return (num/denom) }

Tabla_cluster=as.data.frame(lapply(Tabla_datos[2:6],normalize))
Tabla_cluster=t(Tabla_cluster)
rownames(Tabla_cluster)=c("BTC","ETH","XRP","LTC","BCH")
hc=hclust(dist(as.matrix(Tabla_cluster)))
hc=as.dendrogram(hc)
plot(hc,main = "Agrupamiento",xlab = "Criptomonedas",ylab="Altura",cex=0.6)
rect.dendrogram(hc,  k = 2, border =2:6)


#Calculo la correlacion entre monedas menos parecidas

cor(Tabla_datos$`BTC/Precio`,Tabla_datos$`XRP/Precio`)

#Aunque el valor es menor que a otras correlaciones, en terminos generales es alto.

#Modelo por regresion polinomial de la moneda Bitcoin (BTC). (https://rstudio-pubs-static.s3.amazonaws.com/395717_e8434010c37c4b76bb889020f5e86c2f.html#regresion-polinomial-polynomial-regression)
Tabla_datosNum=Tabla_datos
Tabla_datosNum$Fechas=as.numeric(Tabla_datos$Fechas)
#se eligen observaciones al azar y asignamos una porcion
split = sample.split(Tabla_datosNum$`BTC/Precio`, SplitRatio = 0.7)
nltrain = subset(Tabla_datosNum, split == TRUE)
nltest = subset(Tabla_datosNum, split == FALSE)
nltrain$x2=nltrain$Fechas^3
nltrain$x3=nltrain$Fechas^7
#Se aplica la regresion escribiendo las variables independientes como nombre de columna ya que si las llamamos con nltrain$ da error
regresor_poly=lm(`BTC/Precio` ~ `Fechas`+x2*x3, data = nltrain)
summary(regresor_poly)
#La funcion predict() utiliza el modelo de entrenamiento y lo aplica a un conjunto de datos.
y_poly_predict = predict(regresor_poly, nltrain)
ggplot()+geom_point(data=nltrain,aes(x=as.Date(`Fechas`,origin = "1970-01-01"),y=`BTC/Precio`),size=0.5)+scale_y_log10()+ggtitle("Entrenamiento valor BTC vs tiempo")+geom_line(aes(x=as.Date(nltrain$Fechas,origin = "1970-01-01"),y=y_poly_predict),color="red")+xlab("Tiempo")+ylab("Valor BTC en USD")

#Ahora hacemos lo mismo para el conjunto de datos que separamos para testear el modelo

nltest$x2=nltest$Fechas^3
nltest$x3=nltest$Fechas^7

y_poly_test_predict=predict(regresor_poly,nltest)
summary(y_poly_test_predict)
ggplot()+geom_point(data=nltest,aes(x=as.Date(`Fechas`,origin = "1970-01-01"),y=`BTC/Precio`),size=0.5)+scale_y_log10()+ggtitle("Test valor BTC vs tiempo")+geom_line(aes(x=as.Date(nltest$Fechas,origin = "1970-01-01"),y=y_poly_test_predict),color="red")+xlab("Tiempo")+ylab("Valor BTC en USD")

#"Los resultados del test son similares que el entrenamiento"

#Hay una tendencia positiva del valor con respecto al tiempo, el modelo
#predice dentro de todo bien, con un error cuadrado de 0.85
#Conclusion
#En general hay una buena correlacion entre monedas, pudiendo deducir que el precio del Bitcoin escala de forma
#similar con Ethereum, y caso similar entre Litecoin y Bitcoin Cash. 
#Para el modelado de los datos, la funcion polinomica a rasgos generales representa el ciclo economico
#del Bitcoin, aunque no es muy precisa para obtener datos finos.
# Cluster Analysis
CAG1 <- read_excel("D:/Dhruva/CAG1.xlsx")
attach(CAG1)
z <- CAG1[,-c(1,1)]
z
View(z)
m <- apply(z,2,mean)
m
s <- apply(z,2,sd)
s
z <- scale(z,m,s)
z
distance <- dist(z)
distance
print(distance,digits = 3)
# Cluster Analysis
hc.c<-hclust(distance)
hc.c
# dendrogram
plot(hc.c)
plot(hc.c,hang = -1)
hc.a<-hclust(distance,method = "average")
hc.a
plot(hc.c)
plot(hc.a,hang = -1)
member.c<-cutree(hc.c,3)
member.c
member.a<-cutree(hc.a,3)
table(member.c,member.a)
aggregate(z,list(member.c),mean)
aggregate(CAG1[,-c(1,1)],list(member.c),mean)
# K- means clustoring
library(cluster)
plot(silhouette(cutree(hc.c,3),distance))
kc<-kmeans(z,3)
kc
kc$cluster

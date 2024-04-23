a=20
a
if( a == 20){
  print("Twenty")
} else{
  print("Not twenty")
}

choice = 5
x <- switch(choice,
            "First",
            "second",
            "third",
            "fourth",
)
print(x)


v = c(1,3)
x <- switch(length(v),
            "First",
            "second",
            "third",
            "fourth"
)
print(x)


x1=90
x2=45

x2 <- x1

print(x1)
print(x2)

print(paste(x1,x2))
cat(x1,x2)

v1.x=900

print(ls(pattern="x"))

rm(list=ls())
print(ls())

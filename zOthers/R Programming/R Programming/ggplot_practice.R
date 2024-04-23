
# Format
# ggplot (data = <DATA> ) +
#<GEOM_FUNCTION> (mapping = aes( <MAPPINGS> ))

# geom_functions
# geom_line() , geom_point() , geom_histgram(), 
# geom_col(), geom_bar()
#  geom_boxplot(),  geom_violin(), geom_density()
# 


iris
data = iris

#install.packages("ggplot2")
library(ggplot2)

# Line plot
# describe the trend
ggplot(data, aes(1:150, Sepal.Length)) + geom_line()

# Scatter plot
# Understand relation between x & y
ggplot(data, aes(x = Sepal.Length, y = Sepal.Width)) +
  geom_point()

# Bar chart
ggplot(data, aes(x = Species, y = Sepal.Length)) +
  geom_col()

# Histogram
# Count of each Sepal length occurrence
ggplot(data, aes(x = Sepal.Length)) +
  geom_bar()

# Histogram
# Count of each Sepal length occurrence
# here can control the groups
ggplot(data, aes(Sepal.Length)) +
  geom_histogram(bins = 15)

# Density plot
ggplot(data, aes(Sepal.Length)) +
  geom_density()

# Create a box plot with ggplot2
ggplot(data, aes(x = Sepal.Length)) +  
  geom_boxplot()

# Understand distribution of Sepal length for
# different species
ggplot(data, aes(x = Species, y = Sepal.Length)) +
  geom_violin()


# How to set labels and titles

ggplot(data, aes(x = Sepal.Length, y = Sepal.Width)) +
  geom_point() + labs(x='x axis label', y='y axis label',
                      title='title', subtitle='subtitle',
                      caption='image using ggplot2')



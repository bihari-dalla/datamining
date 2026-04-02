'''
# Practical No. : 09
# Aim: EDA & Data Visualization

# 1. Creating a Data Frame
id <- c(1,2,3,4)
name <- c("Asha", "Rahul", "Neha", "Amit")
marks <- c(85, 90, 78, 88)

df <- data.frame(id, name, marks)
df

# 2. Accessing Data
df$name          # Access column
df[1, ]          # First row
df[, "marks"]    # Specific column
df[1:2, 2:3]     # Subset rows and columns

# 3. To Read data from CSV file to R
Diabetes <- read.csv(file.choose(), header = TRUE, sep = ",")

# 4. To extract first few lines of data set
head(eda_data)

# 5. To check data type of every variable in dataset
str(eda_data)

# 6. To check summary of entire data frame object
summary(eda_data)

# 7. To check first 10 rows of the dataset
eda_data[1:10, ]

# 8. To check only 2 columns of the dataset
eda_data[, 1:2]

# 9. To display first 10 rows and only 2 columns
eda_data[1:10, 1:2]

# 10. Subsetting (single condition)
newdata1 <- subset(EDA_data, EDA_data$Education == "Grad")
newdata1

# 11. Subsetting (multiple conditions)
newdata2 <- subset(EDA_data, EDA_data$Age == "51" & EDA_data$Gender == "M")
newdata2
'''

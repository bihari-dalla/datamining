'''
# 3. Read data from CSV file
# Import dataset from CSV file

EDA_data <- read.csv(file.choose(), header = TRUE, sep = ",")


# 4. Extract first few rows
# head() shows first 6 rows of data

head(EDA_data)


# 5. Check structure of dataset
# str() shows data types and structure

str(EDA_data)


# 6. Summary of dataset
# summary() shows basic statistics

summary(EDA_data)


# 7. Display first 10 rows

EDA_data[1:10, ]


# 8. Display first 2 columns

EDA_data[, 1:2]


# 9. Display first 10 rows and first 2 columns

EDA_data[1:10, 1:2]


# 10. Subsetting (single condition)
# Select rows where Education = "Grad"

newdata1 <- subset(EDA_data, EDA_data$Education == "Grad")
newdata1


# 11. Subsetting (multiple conditions)
# Select rows where Age = 51 and Gender = M

newdata2 <- subset(EDA_data, EDA_data$Age == "51" & EDA_data$Gender == "M")
newdata2


# 12. Sort data in ascending order
# order() sorts column from small to big

newdata4 <- EDA_data[order(EDA_data$Name), ]
newdata4


# Sort using two columns

newdata5 <- EDA_data[order(EDA_data$Education, EDA_data$Salary), ]
newdata5


# 13. Sort data in descending order
# Using minus sign

newdata6 <- EDA_data[order(-EDA_data$Age), ]
newdata6

# Another way using decreasing = TRUE

newdata7 <- EDA_data[order(EDA_data$Age, decreasing = TRUE), ]
newdata7


# 14. Check missing values in dataset

colSums(is.na(EDA_data))   # Count NA values
summary(EDA_data)          # Show summary of data


# 15. Histogram of a column

hist(EDA_data$Age)         # Histogram of Age


# 16. Boxplot of a column

boxplot(EDA_data$Salary)   # Boxplot of Salary


# 17. Basic statistics of column

mean(EDA_data$Salary)      # Average value
median(EDA_data$Salary)    # Middle value
max(EDA_data$Salary)       # Highest value
min(EDA_data$Salary)       # Lowest value


# -----------------------------
# Conversion: Character to Numeric

str <- EDA_data$Gender     # Take Gender column
str

str(EDA_data$Gender)       # Check structure
str(EDA_data$Education)

num <- as.numeric(str)     # Convert to numeric
num

str(num)                   # Structure
typeof(num)                # Type
class(num)                 # Class


# Numeric to Factor

num <- as.factor(num)      # Convert numeric to factor
num
class(num)


# Factor to Character

num <- as.character(num)   # Convert factor to character
num
class(num)
typeof(num)


# Numeric to Logical

v <- c(0,0,1,1)            # Numeric values
v

logi <- as.logical(v)      # Convert to logical
logi


# Logical to Integer

int <- as.integer(logi)    # Convert logical to integer
int
typeof(int)


# Integer to Factor

fact <- as.factor(int)     # Convert integer to factor
fact


# Check structure of Name column

str(EDA_data$Name)         # Structure of Name
'''

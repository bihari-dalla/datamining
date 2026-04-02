'''
# Practical No. : 09
# Aim: EDA & Data Visualization


# 1. Creating a Data Frame
# Creating simple dataset of students

id <- c(1,2,3,4)                  # Student ID
name <- c("Asha","Rahul","Neha","Amit")   # Student names
marks <- c(85,90,78,88)           # Student marks

df <- data.frame(id,name,marks)   # Create data frame
df                                # Display data


# 2. Accessing Data
# Access different parts of data frame

df$name            # Access name column

df[1, ]            # Access first row

df[, "marks"]      # Access marks column

df[1:2, 2:3]       # Access rows 1-2 and columns 2-3
'''

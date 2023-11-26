# run pip install pandas in your terminal before running this
import pandas as pd

"""
This program will ask the user for a programming language and then print
the mean and median salary of people who know that language, as well as
the percentage of people who know that language.
"""

def print_stats(data, lang):
  # find row indices only of rows where the person knows the language, ignore empty values
  lang_used_i = data['LanguageHaveWorkedWith'].str.contains(lang, na=False)

  # get the rows where the person knows the language
  lang_used = data[lang_used_i]

  # get the mean and median salary of the people who know the language, round to 2 decimal places
  mean_salary = lang_used['ConvertedCompYearly'].mean()
  mean_salary = round(mean_salary, 2)

  median_salary = lang_used['ConvertedCompYearly'].median()
  median_salary = round(median_salary, 2)

  # get the percentage of people who know the language
  percentage = round(len(lang_used) / len(data) * 100, 2)

  # print the results
  print("Mean salary: $" + str(mean_salary))
  print("Median salary: $" + str(median_salary))
  print("Percentage of people who know " + lang + ": " + str(percentage) + "%")

def main():
  # load data from csv
  data = pd.read_csv("survey_results_public.csv")

  # extract first 1000 rows for performance (feel free to comment out, but it will take longer to run)
  data = data.head(1000)

  # get input from user
  lang = input("Name a programming language: ")

  # run the function above
  print_stats(data, lang)

main()

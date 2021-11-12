# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Topic: Timestamp class
#
# - Name: Yuelin He
# - UM email: yuelinhe@umich.edu
#

# Timestamp is Pandas' equivalent (and usually interchangeable) class of 
# python’s Datetime. To construct a Timestamp, there are three calling 
# conventions:
#
# 1. Converting a datetime-like string.
#
# 1. Converting a float representing a Unix epoch in units of seconds.
#
# 1. Converting an int representing a Unix-epoch in units of seconds in a 
# specified timezone.
#
# The form accepts four parameters that can be passed by position or keyword.
#
# There are also forms that mimic the API for datetime.datetime (with year, 
# month, day, etc. passed separately through parameters).
#
# See the following code for corresponding examples:
#

# +
import pandas as pd

## datetime-like string
print(pd.Timestamp('2021-01-01T12'))

## float, in units of seconds
print(pd.Timestamp(889088900.5, unit='s'))

##int, in units of seconds, with specified timezone
print(pd.Timestamp(5201314, unit='s', tz='US/Pacific'))
# -

# In Pandas, there are many useful attributes to do quick countings in Timestamp.
#
# - Counting the day of the...
#     + week: using *day_of_week*, *dayofweek*
#     + year: using *day_of_year*, *dayofyear*
# - Counting the week number of the year: using *week*, *weekofyear*
# - Counting the number of days in that month: using *days_in_month*, *daysinmonth*
#

# +
# Counting the day of the week
ts = pd.Timestamp(2018, 3, 21)
print(ts.day_of_week)
print(ts.dayofweek)

# Counting the day of the year
print(ts.day_of_year)
print(ts.dayofyear)

# Counting the week number of the year
print(ts.week)
print(ts.weekofyear)

# Counting the number of days in that month
print(ts.days_in_month)
print(ts.daysinmonth)
# -

# Whether certain characteristic is true can also be determined.
#
# - Deciding if the date is the start of the...
#     + year: using *is_year_start*
#     + quarter: using *is_quarter_start*
#     + month: using *is_month_start*
# - Similarly, deciding if the date is the end of the...
#     + year: using *is_year_end*
#     + quarter: using *is_quarter_end*
#     + month: using *is_month_end*
# - Deciding if the year is a leap year: using *is_leap_year*

# +
# # Start?
print(pd.Timestamp(2000, 1, 1).is_year_start)
print(pd.Timestamp(2000, 2, 1).is_quarter_start)
print(pd.Timestamp(2000, 3, 1).is_month_start)

# # End?
print(pd.Timestamp(2000, 12, 31).is_year_end)
print(pd.Timestamp(2000, 12, 30).is_quarter_end)
print(pd.Timestamp(2000, 11, 30).is_month_start)

# Leap year?
print(pd.Timestamp(2000, 12, 31).is_leap_year)
print(pd.Timestamp(2001, 12, 30).is_leap_year)
# -

#
#
# ##### Reference: 
# https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#

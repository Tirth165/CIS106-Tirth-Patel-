#Input Phase

def calculate_forecast(month, sales):
  forecast_percent = 0.0

  if month in ["Jan", "Feb", "Mar"]:
      forecast_percent = 0.10
  elif month in ["Apr", "May", "Jun"]:
      forecast_percent = 0.15
  elif month in ["Jul", "Aug", "Sep"]:
      forecast_percent = 0.20
  elif month in ["Oct", "Nov", "Dec"]:
      forecast_percent = 0.25

  next_month_sales = sales * (1 + forecast_percent)
  return next_month_sales

#Process

while True:

#output
  
  response = input("Do you want to calculate next month's sales forecast? (Yes/No): ").strip().lower()
  if response != "yes":
      break

  last_name = input("Enter your last name: ")
  month = input("Enter the current month (e.g., Jan, Feb, etc.): ").strip().capitalize()
  sales = float(input("Enter the current sales: $"))

  next_month_sales = calculate_forecast(month, sales)

  print(f"Hello, {last_name}! The forecasted sales for the next month will be: ${next_month_sales:.2f}\n")

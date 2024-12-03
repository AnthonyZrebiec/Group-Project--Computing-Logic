# Funtion to calculate the gross pay based on the hourly rate and hours worked.

def calculates_gross_pay(hourly_rate, hours_worked):
    if hours_worked <= 40: # checks if hours worked is less that or equal to 40, over 40 hours is considered overtime
        return hours_worked * hourly_rate # Calculates gross pay by multiplying hourly rate by hours worked.
    else:
        # If hours worked is greater than 40, overtime pay is calculated.
        overtime_hours = hours_worked - 40 # Calculates overtime hours by subracting 40 from hours worked. 
        return (40 * hourly_rate) + (overtime_hours * hourly_rate * 1.5) # Calculates gross pay by adding overtime pay to regular pay.

# Function to calculate tax deductions based on the gross pay and number of dependents. 

def calculate_deductions(gross_pay, number_of_dependents):
    dependents_deductions = number_of_dependents * 25
    state_tax = gross_pay * 0.056
    federal_tax = gross_pay * 0.079

    pre_tax_amount = gross_pay - dependents_deduction
    post_tax_amount = post_tax_amount - (state_tax + federal_tax)

    # Return values including dependents deduction, state tax, federal tax, and post-tax amount.
    return{
        'dependents_deduction': dependents_deduction,
        'state_tax': state_tax,
        'post_tax_amount': post_tax_amount
    }

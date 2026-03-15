"""
Financial Calculator Suite
A comprehensive tool for stock trading commission calculations and financial analysis
"""


# ==================== CALCULATION FUNCTIONS ====================

def calculate_gross_profit(sell_price, buy_price, shares):
    """Calculate gross profit from stock transaction."""
    return sell_price * shares - buy_price * shares


def calculate_commission(price, shares, commission_rate, minimum=5.0):
    """
    Calculate commission fee with minimum threshold.

    Args:
        price: Transaction price per share
        shares: Number of shares
        commission_rate: Commission rate (e.g., 0.0003 for 0.03%)
        minimum: Minimum commission fee (default 5 CNY)

    Returns:
        Commission fee amount
    """
    commission = price * shares * commission_rate
    return commission if commission > minimum else minimum


def calculate_annual_rate(principal, days, profit):
    """
    Calculate annual percentage rate (APR).

    Formula: APR = (profit / days) * 365 / principal * 100
    """
    return profit / days * 365 / principal * 100


def calculate_profit_from_rate(principal, days, annual_rate):
    """
    Calculate profit from annual rate.

    Formula: Profit = principal * annual_rate / 365 * days / 100
    """
    return principal * annual_rate / 365 * days / 100


def calculate_golden_ratio_level(base_price, multiplier):
    """Calculate price level using golden ratio multiplier."""
    return base_price * multiplier


def calculate_support_resistance(high_point, low_point, ratio):
    """
    Calculate support and resistance levels using golden ratio.

    Args:
        high_point: Highest price in the period
        low_point: Lowest price in the period
        ratio: Golden ratio multiplier

    Returns:
        Tuple of (support_level, resistance_level)
    """
    price_range = high_point - low_point
    support_level = high_point - price_range * ratio
    resistance_level = support_level + price_range * (1 + ratio)
    return support_level, resistance_level


# ==================== BRANCH HANDLERS ====================

def branch_1_commission_calculator():
    """
    Branch 1: Stock Trading Commission Calculator (Chinese Market)

    Calculates:
    - Gross Profit
    - Stamp Duty (0.1% on sell only)
    - Transfer Fees
    - Commissions (minimum 5 CNY rule)
    - Determines if trade yields "Real Profit" or "Donated Profit"
    """
    try:
        # Input
        buy_price = float(input("Buy price per share: "))
        sell_price = float(input("Sell price per share: "))
        shares = float(input("Number of shares: "))
        print()

        # Constants (Chinese market specific)
        COMMISSION_RATE = 0.0003      # 0.03% commission rate (set by broker)
        TRANSFER_FEE_RATE = 0.00002   # 0.002% transfer fee (national standard)
        STAMP_DUTY_RATE = 0.001       # 0.1% stamp duty (national standard)
        MINIMUM_COMMISSION = 5.0      # Minimum 5 CNY commission

        # Calculations
        gross_profit = calculate_gross_profit(sell_price, buy_price, shares)
        print(f"Gross Profit: {gross_profit:.2f} CNY")

        # Buy-side fees
        commission_buy = calculate_commission(buy_price, shares, COMMISSION_RATE, MINIMUM_COMMISSION)
        print(f"Commission (Buy): {commission_buy:.2f} CNY")

        # Sell-side fees
        commission_sell = calculate_commission(sell_price, shares, COMMISSION_RATE, MINIMUM_COMMISSION)
        print(f"Commission (Sell): {commission_sell:.2f} CNY")

        # Stamp duty (only on sell)
        stamp_duty = sell_price * shares * STAMP_DUTY_RATE
        print(f"Stamp Duty: {stamp_duty:.2f} CNY")

        # Transfer fees
        transfer_fee_buy = buy_price * shares * TRANSFER_FEE_RATE
        print(f"Transfer Fee (Buy): {transfer_fee_buy:.2f} CNY")

        transfer_fee_sell = sell_price * shares * TRANSFER_FEE_RATE
        print(f"Transfer Fee (Sell): {transfer_fee_sell:.2f} CNY")

        # Total fees breakdown
        total_buy_fees = commission_buy + transfer_fee_buy
        print(f"Total Buy Fees: {total_buy_fees:.2f} CNY")

        total_sell_fees = commission_sell + transfer_fee_sell + stamp_duty
        print(f"Total Sell Fees: {total_sell_fees:.2f} CNY")

        total_fees = round(total_buy_fees + total_sell_fees, 2)
        print(f"Total Fees: {total_fees} CNY")

        # Net profit
        net_profit = round(gross_profit - total_fees, 2)
        print(f"Net Profit: {net_profit} CNY")

        # Profit type determination
        if net_profit >= total_fees:
            print("Net Profit >= Total Fees → Real Profit")
        else:
            print("Net Profit < Total Fees → Donated Profit")

        print('\n' * 2)

    except Exception as err:
        print(f"Error: {err}")


def branch_2_golden_ratio_single_base():
    """
    Branch 2: Golden Ratio Price Levels (Single Base Point)

    Uses Fibonacci/Golden Ratio multipliers to calculate support and resistance levels.
    The levels metaphorically correspond to Yoga Chakras (Root, Sacral, etc.)
    """
    base_price = float(input("Enter base price (period high or low): "))
    print(f"Base Price: {base_price}")
    print('------- Finding Resistance in Uptrend -------\n')

    # Upside resistance levels (Crown to Root chakra)
    print(f"Base Price × 1.809 (Crown Chakra), Level +7: {calculate_golden_ratio_level(base_price, 1.809):.2f}\n")
    print(f"Base Price × 1.764 (Third Eye Chakra), Level +6: {calculate_golden_ratio_level(base_price, 1.764):.2f}\n")
    print(f"Base Price × 1.618 (Throat Chakra), Level +5: {calculate_golden_ratio_level(base_price, 1.618):.2f}\n")
    print(f"Base Price × 1.500 (Heart Chakra), Level +4: {calculate_golden_ratio_level(base_price, 1.500):.2f}\n")
    print(f"Base Price × 1.382 (Solar Plexus Chakra), Level +3: {calculate_golden_ratio_level(base_price, 1.382):.2f}\n")
    print(f"Base Price × 1.236 (Sacral Chakra), Level +2: {calculate_golden_ratio_level(base_price, 1.236):.2f}\n")
    print(f"Base Price × 1.191 (Root Chakra), Level +1: {calculate_golden_ratio_level(base_price, 1.191):.2f}\n")

    print('------- Finding Support in Downtrend -------\n')

    # Downside support levels (Root to Crown chakra)
    print(f"Base Price × 0.809 (Root Chakra), Level -1: {calculate_golden_ratio_level(base_price, 0.809):.2f}\n")
    print(f"Base Price × 0.764 (Sacral Chakra), Level -2: {calculate_golden_ratio_level(base_price, 0.764):.2f}\n")
    print(f"Base Price × 0.618 (Solar Plexus Chakra), Level -3: {calculate_golden_ratio_level(base_price, 0.618):.2f}\n")
    print(f"Base Price × 0.500 (Heart Chakra), Level -4: {calculate_golden_ratio_level(base_price, 0.500):.2f}\n")
    print(f"Base Price × 0.382 (Throat Chakra), Level -5: {calculate_golden_ratio_level(base_price, 0.382):.2f}\n")
    print(f"Base Price × 0.236 (Third Eye Chakra), Level -6: {calculate_golden_ratio_level(base_price, 0.236):.2f}\n")
    print(f"Base Price × 0.191 (Crown Chakra), Level -7: {calculate_golden_ratio_level(base_price, 0.191):.2f}\n")


def branch_3_golden_ratio_dual_base():
    """
    Branch 3: Golden Ratio Price Levels (Dual Base Points)

    Uses high and low points to calculate support and resistance using golden ratios.
    Seven levels corresponding to the seven Chakras.
    """
    high_point = float(input("Enter high point: "))
    low_point = float(input("Enter low point: "))

    print(f"--- High Point ---: {high_point}")
    print(f"--- Low Point ---: {low_point}\n")

    # Seven levels (chakras) with their golden ratio multipliers
    levels = [
        ("Root Chakra", 0.191, 1.191),
        ("Sacral Chakra", 0.236, 1.236),
        ("Solar Plexus Chakra", 0.382, 1.382),
        ("Heart Chakra", 0.500, 1.500),
        ("Throat Chakra", 0.618, 1.618),
        ("Third Eye Chakra", 0.764, 1.764),
        ("Crown Chakra", 0.809, 1.809)
    ]

    for i, (chakra_name, ratio_down, ratio_up) in enumerate(levels, 1):
        print(f"--- Level {i} ({chakra_name}): {ratio_down} & {ratio_up} ---")
        support, resistance = calculate_support_resistance(high_point, low_point, ratio_down)
        print(f"Downtrend Support: {support:.2f}")
        print(f"Uptrend Resistance: {resistance:.2f}\n")


def branch_4_calculate_apr_from_profit():
    """
    Branch 4: Calculate Annual Percentage Rate (APR)

    Input: Principal, Days, Profit
    Output: Annual Percentage Rate (%)
    """
    print("Calculate APR from Principal, Days, and Profit\n")

    try:
        principal = float(input("Principal: "))
        days = int(input("Number of days: "))
        profit = float(input("Profit: "))
        print()

        apr = calculate_annual_rate(principal, days, profit)
        print(f"Annual Percentage Rate (APR): {apr}%")

    except Exception as err:
        print(f"Error: {err}")


def branch_5_calculate_profit_from_apr():
    """
    Branch 5: Calculate Profit from APR

    Input: Annual Percentage Rate (%), Principal, Days
    Output: Profit
    """
    print("Calculate Profit from APR, Principal, and Days\n")

    try:
        annual_rate = float(input("Annual Percentage Rate (%): "))
        days = int(input("Number of days: "))
        principal = float(input("Principal: "))
        print()

        profit = calculate_profit_from_rate(principal, days, annual_rate)
        print(f"Profit (Interest): {profit} CNY")

    except Exception as err:
        print(f"Error: {err}")


def branch_6_apr_from_daily_profit_fixed():
    """
    Branch 6: Calculate APR from Daily Profit (Fixed Principal)

    Input: Daily Profit
    Output: Annual Percentage Rate (%)
    Note: Principal is fixed at 10,000 CNY
    """
    print("Calculate APR from Daily Profit (Principal fixed at 10,000 CNY)\n")

    try:
        daily_profit = float(input("Daily Profit (CNY): "))
        principal = 10000.00
        print()

        # Calculate annual profit from daily profit
        annual_profit = daily_profit * 365

        # Calculate APR
        apr = calculate_annual_rate(principal, 365, annual_profit)
        print(f"Annual Percentage Rate (APR): {apr}%")

    except Exception as err:
        print(f"Error: {err}")


def branch_7_daily_profit_from_apr():
    """
    Branch 7: Calculate Daily Profit from Principal and APR

    Input: Annual Percentage Rate (%), Principal
    Output: Daily Profit (Daily Interest)
    """
    print("Calculate Daily Profit from Principal and APR\n")

    try:
        annual_rate = float(input("Annual Percentage Rate (%): "))
        principal = float(input("Principal: "))
        print()

        # Calculate for 1 day
        daily_profit = calculate_profit_from_rate(principal, 1, annual_rate)
        print(f"Daily Profit (Daily Interest): {daily_profit} CNY")

    except Exception as err:
        print(f"Error: {err}")


def branch_8_apr_from_daily_profit():
    """
    Branch 8: Calculate APR from Principal and Daily Profit

    Input: Principal, Daily Profit
    Output: Annual Percentage Rate (%)
    """
    print("Calculate APR from Principal and Daily Profit\n")

    try:
        daily_profit = float(input("Daily Profit (CNY): "))
        principal = float(input("Principal: "))
        print()

        # Calculate annual profit from daily profit
        annual_profit = daily_profit * 365

        # Calculate APR
        apr = calculate_annual_rate(principal, 365, annual_profit)
        print(f"Annual Percentage Rate (APR): {apr}%")

    except Exception as err:
        print(f"Error: {err}")


# ==================== MENU AND MAIN PROGRAM ====================

def display_menu():
    """Display the main menu of available calculators."""
    print("\n" + "=" * 60)
    print("         FINANCIAL CALCULATOR SUITE")
    print("=" * 60)
    print("1 - Commission Calculator (Stock Trading)")
    print("2 - Golden Ratio Levels (Single Base Point)")
    print("3 - Golden Ratio Levels (Dual Base Points)")
    print("4 - Calculate APR from Principal, Days, and Profit")
    print("5 - Calculate Profit from APR, Principal, and Days")
    print("6 - Calculate APR from Daily Profit (Fixed 10K Principal)")
    print("7 - Calculate Daily Profit from Principal and APR")
    print("8 - Calculate APR from Principal and Daily Profit")
    print("0 - Exit")
    print("=" * 60)


def main():
    """Main program loop with menu-driven interface."""

    # Menu dispatcher - maps choices to handler functions
    menu_handlers = {
        1: branch_1_commission_calculator,
        2: branch_2_golden_ratio_single_base,
        3: branch_3_golden_ratio_dual_base,
        4: branch_4_calculate_apr_from_profit,
        5: branch_5_calculate_profit_from_apr,
        6: branch_6_apr_from_daily_profit_fixed,
        7: branch_7_daily_profit_from_apr,
        8: branch_8_apr_from_daily_profit
    }

    print("\nWelcome to the Financial Calculator Suite!")

    while True:
        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 0:
                print("\nThank you for using the Financial Calculator Suite!")
                print("Goodbye!")
                break

            if choice in menu_handlers:
                print("\n" + "-" * 60)
                menu_handlers[choice]()
                print("-" * 60)
            else:
                print("\nInvalid choice. Please select a number from 0 to 8.")

        except ValueError:
            print("\nInvalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            print("Goodbye!")
            break
        except Exception as err:
            print(f"\nUnexpected error: {err}")


if __name__ == "__main__":
    main()


"""
NOTES ON CHAKRAS (Energy Centers):

From bottom to top, the seven chakras are:
1. Root Chakra (Mooladhara Chakra) - Grounding, stability
2. Sacral Chakra (Swadhisthan Chakra) - Creativity, emotions
3. Solar Plexus Chakra (Nabhi/Manipura Chakra) - Power, confidence
   3a. Void (Ocean of Illusion) - Between solar plexus and heart
4. Heart Chakra (Anahata Chakra) - Love, compassion
5. Throat Chakra (Vishuddhi Chakra) - Communication, expression
6. Third Eye Chakra (Agnya/Ajna Chakra) - Intuition, insight
7. Crown Chakra (Sahasrara Chakra) - Spiritual connection, enlightenment

These metaphors are used in technical analysis to represent different
price levels based on golden ratio (Fibonacci) multipliers.
"""

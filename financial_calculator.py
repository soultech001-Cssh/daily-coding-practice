"""
Financial Calculator
Stock commission calculation, golden ratio analysis, and APR calculations.
"""

# =============================================================================
# CONSTANTS - Chinese Stock Market Rates
# =============================================================================

COMMISSION_RATE = 0.0003      # Brokerage commission rate (varies by broker)
TRANSFER_FEE_RATE = 0.00002   # Transfer fee rate (set by government)
STAMP_DUTY_RATE = 0.001       # Stamp duty rate (only on sell, set by government)
MIN_COMMISSION = 5            # Minimum commission per transaction (CNY)

# Golden ratio levels (based on Fibonacci ratios)
GOLDEN_RATIOS = [
    (0.191, 1.191, "Level 1"),
    (0.236, 1.236, "Level 2"),
    (0.382, 1.382, "Level 3"),
    (0.500, 1.500, "Level 4"),
    (0.618, 1.618, "Level 5"),
    (0.764, 1.764, "Level 6"),
    (0.809, 1.809, "Level 7"),
]


# =============================================================================
# COMMISSION CALCULATION FUNCTIONS
# =============================================================================

def calculate_gross_profit(sell_price, buy_price, share_volume):
    """Calculate gross profit from stock trade."""
    return sell_price * share_volume - buy_price * share_volume


def calculate_commission(price, share_volume, commission_rate=COMMISSION_RATE):
    """
    Calculate brokerage commission with minimum threshold.
    Chinese stock market rule: minimum commission is 5 CNY.
    """
    calculated = price * share_volume * commission_rate
    return max(calculated, MIN_COMMISSION)


def calculate_stamp_duty(sell_price, share_volume, stamp_duty_rate=STAMP_DUTY_RATE):
    """
    Calculate stamp duty (only applied on sell transactions).
    Chinese stock market rule: stamp duty only charged when selling.
    """
    return sell_price * share_volume * stamp_duty_rate


def calculate_transfer_fee(price, share_volume, transfer_fee_rate=TRANSFER_FEE_RATE):
    """Calculate transfer fee for a transaction."""
    return price * share_volume * transfer_fee_rate


def calculate_trading_costs(buy_price, sell_price, share_volume):
    """
    Calculate all trading costs for a round-trip trade.
    Returns a dictionary with detailed breakdown.
    """
    # Buy side costs
    commission_buy = calculate_commission(buy_price, share_volume)
    transfer_fee_buy = calculate_transfer_fee(buy_price, share_volume)
    cost_buy = commission_buy + transfer_fee_buy

    # Sell side costs (includes stamp duty)
    commission_sell = calculate_commission(sell_price, share_volume)
    transfer_fee_sell = calculate_transfer_fee(sell_price, share_volume)
    stamp_duty = calculate_stamp_duty(sell_price, share_volume)
    cost_sell = commission_sell + transfer_fee_sell + stamp_duty

    # Total costs
    total_cost = cost_buy + cost_sell

    return {
        "commission_buy": commission_buy,
        "commission_sell": commission_sell,
        "transfer_fee_buy": transfer_fee_buy,
        "transfer_fee_sell": transfer_fee_sell,
        "stamp_duty": stamp_duty,
        "cost_buy": cost_buy,
        "cost_sell": cost_sell,
        "total_cost": total_cost,
    }


# =============================================================================
# GOLDEN RATIO FUNCTIONS
# =============================================================================

def calculate_golden_ratio_single(base_price):
    """
    Calculate golden ratio levels from a single base price.
    Used for finding resistance (uptrend) and support (downtrend) levels.
    """
    results = {"resistance": [], "support": []}

    for down_ratio, up_ratio, level_name in GOLDEN_RATIOS:
        results["resistance"].append({
            "level": level_name,
            "ratio": up_ratio,
            "price": round(base_price * up_ratio, 2),
        })
        results["support"].append({
            "level": level_name,
            "ratio": down_ratio,
            "price": round(base_price * down_ratio, 2),
        })

    return results


def calculate_golden_ratio_dual(high_point, low_point):
    """
    Calculate golden ratio levels from two base points (high and low).
    Calculates support and resistance based on the price range.
    """
    price_range = high_point - low_point
    results = []

    for down_ratio, up_ratio, level_name in GOLDEN_RATIOS:
        support = high_point - price_range * down_ratio
        resistance = support + price_range * up_ratio
        results.append({
            "level": level_name,
            "down_ratio": down_ratio,
            "up_ratio": up_ratio,
            "support": round(support, 2),
            "resistance": round(resistance, 2),
        })

    return results


# =============================================================================
# APR (ANNUAL PERCENTAGE RATE) FUNCTIONS
# =============================================================================

def calculate_apr_from_profit(principal, days, profit):
    """
    Calculate annual percentage rate from principal, days, and profit.
    Formula: APR = (profit / days * 365 / principal) * 100
    """
    return (profit / days * 365 / principal) * 100


def calculate_profit_from_apr(principal, days, apr):
    """
    Calculate profit from principal, days, and annual percentage rate.
    Formula: profit = principal * apr / 100 / 365 * days
    """
    return principal * apr / 100 / 365 * days


def calculate_daily_income(principal, apr):
    """
    Calculate daily income from principal and annual percentage rate.
    Formula: daily_income = principal * apr / 100 / 365
    """
    return principal * apr / 100 / 365


def calculate_apr_from_daily_income(principal, daily_income):
    """
    Calculate annual percentage rate from principal and daily income.
    Formula: APR = (daily_income * 365 / principal) * 100
    """
    return (daily_income * 365 / principal) * 100


# =============================================================================
# MENU HANDLER FUNCTIONS
# =============================================================================

def handle_commission_calculation():
    """Handle stock commission calculation (Menu option 1)."""
    try:
        print("\n--- Stock Commission Calculator ---\n")
        buy_price = float(input("Buy price: "))
        sell_price = float(input("Sell price: "))
        share_volume = float(input("Share volume: "))
        print()

        # Calculate gross profit
        gross_profit = calculate_gross_profit(sell_price, buy_price, share_volume)

        # Calculate all trading costs
        costs = calculate_trading_costs(buy_price, sell_price, share_volume)

        # Calculate net profit
        net_profit = gross_profit - costs["total_cost"]

        # Display results
        print(f"Gross Profit: {gross_profit:.2f} CNY")
        print(f"Commission (Buy): {costs['commission_buy']:.2f} CNY")
        print(f"Commission (Sell): {costs['commission_sell']:.2f} CNY")
        print(f"Stamp Duty: {costs['stamp_duty']:.2f} CNY")
        print(f"Transfer Fee (Buy): {costs['transfer_fee_buy']:.2f} CNY")
        print(f"Transfer Fee (Sell): {costs['transfer_fee_sell']:.2f} CNY")
        print(f"Total Cost (Buy): {costs['cost_buy']:.2f} CNY")
        print(f"Total Cost (Sell): {costs['cost_sell']:.2f} CNY")
        print(f"Total Trading Cost: {costs['total_cost']:.2f} CNY")
        print(f"Net Profit: {net_profit:.2f} CNY")

        # Profit analysis
        if net_profit >= costs["total_cost"]:
            print("Result: Net profit >= Trading cost (Profitable trade)")
        else:
            print("Result: Net profit < Trading cost (Costs exceed profit)")

    except Exception as err:
        print(f"Error: {err}")


def handle_golden_ratio_single():
    """Handle golden ratio calculation with single base point (Menu option 2)."""
    print("\n--- Golden Ratio Calculator (Single Base Point) ---\n")
    base_price = float(input("Enter base price: "))
    print(f"\nBase Price: {base_price}")

    results = calculate_golden_ratio_single(base_price)

    print("\n--- Resistance Levels (Uptrend) ---\n")
    for item in reversed(results["resistance"]):
        print(f"Base * {item['ratio']:.3f} ({item['level']}): {item['price']} CNY")

    print("\n--- Support Levels (Downtrend) ---\n")
    for item in results["support"]:
        print(f"Base * {item['ratio']:.3f} ({item['level']}): {item['price']} CNY")


def handle_golden_ratio_dual():
    """Handle golden ratio calculation with dual base points (Menu option 3)."""
    print("\n--- Golden Ratio Calculator (Dual Base Points) ---\n")
    high_point = float(input("Enter high point: "))
    low_point = float(input("Enter low point: "))

    print(f"\n--- High Point: {high_point} ---")
    print(f"--- Low Point: {low_point} ---\n")

    results = calculate_golden_ratio_dual(high_point, low_point)

    for item in results:
        print(f"--- {item['level']}: {item['down_ratio']} & {item['up_ratio']} ---")
        print(f"Support Level: {item['support']}")
        print(f"Resistance Level: {item['resistance']}")
        print()


def handle_apr_from_profit():
    """Calculate APR from principal, days, and profit (Menu option 4)."""
    print("\n--- Calculate APR from Principal, Days, and Profit ---\n")
    principal = float(input("Principal: "))
    days = int(input("Number of days: "))
    profit = float(input("Profit: "))
    print()

    try:
        apr = calculate_apr_from_profit(principal, days, profit)
        print(f"Annual Percentage Rate (APR): {apr:.4f}%")
    except Exception as err:
        print(f"Error: {err}")


def handle_profit_from_apr():
    """Calculate profit from APR, days, and principal (Menu option 5)."""
    print("\n--- Calculate Profit from APR, Days, and Principal ---\n")
    apr = float(input("APR (%): "))
    days = int(input("Number of days: "))
    principal = float(input("Principal: "))
    print()

    try:
        profit = calculate_profit_from_apr(principal, days, apr)
        print(f"Profit (Interest): {profit:.4f} CNY")
    except Exception as err:
        print(f"Error: {err}")


def handle_apr_from_daily_fixed_principal():
    """Calculate APR from daily income with fixed 10,000 principal (Menu option 6)."""
    print("\n--- Calculate APR from Daily Income (Principal = 10,000) ---\n")
    daily_income = float(input("Daily income (CNY): "))
    principal = 10000.00
    print()

    try:
        apr = calculate_apr_from_daily_income(principal, daily_income)
        print(f"Annual Percentage Rate (APR): {apr:.4f}%")
    except Exception as err:
        print(f"Error: {err}")


def handle_daily_income_from_apr():
    """Calculate daily income from principal and APR (Menu option 7)."""
    print("\n--- Calculate Daily Income from Principal and APR ---\n")
    apr = float(input("APR (%): "))
    principal = float(input("Principal: "))
    print()

    try:
        daily_income = calculate_daily_income(principal, apr)
        print(f"Daily Income: {daily_income:.4f} CNY")
    except Exception as err:
        print(f"Error: {err}")


def handle_apr_from_daily_custom_principal():
    """Calculate APR from principal and daily income (Menu option 8)."""
    print("\n--- Calculate APR from Principal and Daily Income ---\n")
    daily_income = float(input("Daily income (CNY): "))
    principal = float(input("Principal: "))
    print()

    try:
        apr = calculate_apr_from_daily_income(principal, daily_income)
        print(f"Annual Percentage Rate (APR): {apr:.4f}%")
    except Exception as err:
        print(f"Error: {err}")


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("        FINANCIAL CALCULATOR MENU")
    print("=" * 50)
    print("1 - Stock Commission Calculator")
    print("2 - Golden Ratio Analysis (Single Base Point)")
    print("3 - Golden Ratio Analysis (Dual Base Points)")
    print("4 - Calculate APR from Principal, Days, Profit")
    print("5 - Calculate Profit from APR, Days, Principal")
    print("6 - Calculate APR from Daily Income (Principal=10,000)")
    print("7 - Calculate Daily Income from Principal and APR")
    print("8 - Calculate APR from Principal and Daily Income")
    print("0 - Exit")
    print("=" * 50)


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    """Main program loop."""
    menu_handlers = {
        1: handle_commission_calculation,
        2: handle_golden_ratio_single,
        3: handle_golden_ratio_dual,
        4: handle_apr_from_profit,
        5: handle_profit_from_apr,
        6: handle_apr_from_daily_fixed_principal,
        7: handle_daily_income_from_apr,
        8: handle_apr_from_daily_custom_principal,
    }

    while True:
        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 0:
                print("\nGoodbye!")
                break
            elif choice in menu_handlers:
                menu_handlers[choice]()
            else:
                print("\nInvalid input. Please enter a number from 0 to 8.")

        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

        print("\n" + "-" * 50)


if __name__ == "__main__":
    main()

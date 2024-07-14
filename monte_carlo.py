import numpy as np

def monte_carlo_option_pricing(S0, K, T, r, sigma, num_simulations):
    np.random.seed(0)
    dt = T
    discount_factor = np.exp(-r * T)
    call_option_prices = []
    put_option_prices = []

    for _ in range(num_simulations):
        S_T = S0 * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * np.random.randn())
        call_option_price = max(S_T - K, 0)
        put_option_price = max(K - S_T, 0)
        call_option_prices.append(call_option_price)
        put_option_prices.append(put_option_price)

    call_price_estimate = discount_factor * np.mean(call_option_prices)
    put_price_estimate = discount_factor * np.mean(put_option_prices)
    return call_price_estimate, put_price_estimate

S0 = 100
K = 105
T = 1
r = 0.05
sigma = 0.2
num_simulations = 100000

estimated_call_price, estimated_put_price = monte_carlo_option_pricing(S0, K, T, r, sigma, num_simulations)

print(f"Put price using monte carlo: {estimated_put_price:.2f}")
print(f"Call price using monte carlo: {estimated_call_price:.2f}")

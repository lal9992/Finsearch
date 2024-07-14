import numpy as np

S0 = 100
K = 105
T = 1.0
r = 0.05
sigma = 0.2
num_simulations = 1000000

z = np.random.standard_normal(num_simulations)
ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * z)
call_payoffs = np.maximum(ST - K, 0)
put_payoffs = np.maximum(K - ST, 0)
discounted_call_payoffs = np.exp(-r * T) * call_payoffs
discounted_put_payoffs = np.exp(-r * T) * put_payoffs
call_option_price = np.mean(discounted_call_payoffs)
put_option_price = np.mean(discounted_put_payoffs)

print(f"Estimated European Put Option Price: {put_option_price:.2f}")
print(f"Estimated European Call Option Price: {call_option_price:.2f}")

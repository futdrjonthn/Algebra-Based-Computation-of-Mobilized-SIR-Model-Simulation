import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

mobility_matrix = np.array([
    [0.95, 0.025, 0.025],
    [0.025, 0.95, 0.025],
    [0.025, 0.025, 0.95],
])

def simulate_new_recoveries(recovery_rate,  infected_people):
    return np.random.binomial(infected_people, recovery_rate)

def simulate_new_infected(infection_rate, suspectible_people, infected_people, total_people):
    infection_prob = infection_rate * (infected_people / total_people)
    return np.random.binomial(suspectible_people, infection_prob)

def run_simulation():
    suspectible_people_list = []
    infected_people_list = []
    recovered_people_list = []
    time_list = []

    suspectible_people = np.array([299, 400, 500], dtype=float)
    infected_people = np.array([1, 0, 0], dtype=float)
    recovered_people = np.array([0, 0, 0], dtype=float)

    infection_rate = 0.5
    recovery_rate = 0.1

    count = 1

    for i in range(300):
        suspectible_people_list.append(suspectible_people.copy())
        infected_people_list.append(infected_people.copy())
        recovered_people_list.append(recovered_people.copy())
        time_list.append(count)

        suspectible_people = mobility_matrix @ suspectible_people
        infected_people = mobility_matrix @ infected_people
        recovered_people = mobility_matrix @ recovered_people

        total_people = suspectible_people + infected_people + recovered_people

        new_recoveries = simulate_new_recoveries(recovery_rate, infected_people.astype(int))
        new_infected = simulate_new_infected(infection_rate, suspectible_people.astype(int), infected_people, total_people)

        suspectible_people = suspectible_people - new_infected
        infected_people = infected_people + new_infected - new_recoveries
        recovered_people = recovered_people + new_recoveries

        count += 1

    return {
        'suspectible': np.stack(suspectible_people_list),
        'infected': np.stack(infected_people_list),
        'recovered': np.stack(recovered_people_list),
        'time': time_list
    }

results = run_simulation()

results_s = np.array(results['suspectible'])
results_i = np.array(results['infected'])
results_r = np.array(results['recovered'])

plt.plot(results['time'], results_s.sum(axis=1), label='Susceptible')
plt.plot(results['time'], results_i.sum(axis=1), label='Infected')
plt.plot(results['time'], results_r.sum(axis=1), label='Recovered')
plt.xlabel("Time")
plt.ylabel("Number of People")
plt.legend()
plt.grid(True)
plt.title("SIR Model Simulation with Mobility")
plt.show(block=False)
plt.pause(0.1)

plt.figure(figsize=(10, 6))
sns.heatmap(results_r.T, cmap="RdYlGn", cbar_kws={'label': 'Recovered Count'})
plt.xlabel("Time Step")
plt.ylabel("Region")
plt.title("Heatmap of Recovered People Per Region Over Time")
plt.tight_layout()
plt.show(block=False)
plt.pause(0.1)

input("Press Enter to exit and close all plots...")
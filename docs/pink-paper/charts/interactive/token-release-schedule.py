import matplotlib.pyplot as plt

# Time points for the weekly intervals (assuming 260 weeks in 5 years)
weeks = list(range(1, 261))

# Token release data per week assuming linear release post-initial distribution
players_initial = 2_000_000
players_weekly = (200_000_000 + 100_000_000 + 195_000_000 - players_initial) / (260 - 1) / 4
verifiers_initial = 2_000_000
verifiers_weekly = (2_970_000_000 - verifiers_initial) / (260 - 1) / 4
reserve_initial = 45_000_000
reserve_weekly = (2_970_000_000 - reserve_initial) / (260 - 1) / 4
developers_initial = 200_000
developers_weekly = (990_000_000 - developers_initial) / (260 - 1) / 4
community_initial = 800_000
community_weekly = (1_485_000_000 - community_initial) / (260 - 1) / 4
liquidity_initial = 50_000_000
liquidity_weekly = (990_000_000 - liquidity_initial) / (260 - 1) / 4

# Calculating weekly releases and cumulative sums for each group over weeks
players = [players_initial if week == 1 else players_weekly for week in weeks]
players_cumulative = [sum(players[:week]) for week in range(len(weeks))]
verifiers = [verifiers_initial if week == 1 else verifiers_weekly for week in weeks]
verifiers_cumulative = [sum(verifiers[:week]) for week in range(len(weeks))]
reserve = [reserve_initial if week == 1 else reserve_weekly for week in weeks]
reserve_cumulative = [sum(reserve[:week]) for week in range(len(weeks))]
developers = [developers_initial if week == 1 else developers_weekly for week in weeks]
developers_cumulative = [sum(developers[:week]) for week in range(len(weeks))]
community = [community_initial if week == 1 else community_weekly for week in weeks]
community_cumulative = [sum(community[:week]) for week in range(len(weeks))]
liquidity = [liquidity_initial if week == 1 else liquidity_weekly for week in weeks]
liquidity_cumulative = [sum(liquidity[:week]) for week in range(len(weeks))]

# Plotting the cumulative chart in dark mode
plt.figure(figsize=(12, 7))
plt.style.use('dark_background')
plt.stackplot(weeks, players_cumulative, verifiers_cumulative, reserve_cumulative, developers_cumulative, community_cumulative, liquidity_cumulative, labels=['Players', 'Verifiers', 'Reserve', 'Developers', 'Community', 'Liquidity Pools'], colors=['#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4'])
plt.title('Cumulative Token Release Schedule for BLUV Over 5 Years (Weekly)')
plt.xlabel('Weeks')
plt.ylabel('Total Tokens Released (cumulative)')
plt.legend(loc='upper left')
plt.show()

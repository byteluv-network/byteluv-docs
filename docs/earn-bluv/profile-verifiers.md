---
sidebar_position: 2
---

# Profile Verifiers

Earn $BLUV by verifying profiles on ByteLuv. Every profile will need to be verified by a verifier before they can play the game.

## Pre-requisite

Every verifier will need to have:
1. A minimum of 10,000 \$BLUV tokens in their wallet **[locked](../byteLuv-tutorial/terminologies-of-byteluv.md#lock)**.
2. Verify at least 10 players per week.
3. Maintain a reputation score of 80% or higher.

## Role

Make sure and check the authenticity of the players in the ByteLuv ecosystem.

## How to Verify

### Step 1: Verify Profile

Check the profile of the player to ensure it is genuine
  - **Photo**: Verify the photo of the player.
  - **Bio**: Verify the bio of the player.
  - **Social Links**: Verify the social links of the player.
      - Instagram & Telegram
  - **Verification**: Verify the player's information:
      - Location - country and city
  - **Mark as Verified**: 
      - Mark the player as verified if all the information is correct.
      - If any information is incorrect, mark the player as suspicious and flag the issue.

### Step 2: Verification Status

Set the verification status of the player based on the information.
    - **Verified**: If the player is genuine.
    - **Suspicious**: If the player is suspicious.

### Step 3: Verification Process
Every player must be verified by at least 3 verifiers to be considered verified. The verification is calculated based on the following factors:
    - 2 out of 3 verifiers must approve the player to be considered verified.
    - Anything less than 2/3 approval rate:
      - 3 more verifiers will be assigned to verify the player.
      - If the player is still not verified, the player will not be verified.
  
## Rewards
100 \$BLUV tokens will allocated for the verification of a player. The rewards will be distributed equally to all verifiers involved in the verification process.

## Reputation Score
To ensure validators are honest and accurate, a reputation system is implemented. The reputation score is calculated based on the verifier's accuracy in verifying players and voting on suspicious activity.

### Reputation Score
Reputation is a score that is calculated based on the following factors:
    1. **Verification Accuracy**: The percentage of players verified correctly.
    2. **Activity**: The number of players verified and voted on.
    3. **Voting Accuracy**: The percentage of players voted correctly.

### Calculation
The reputation score is calculated as follows:
    1. **Initial Reputation**: 100%
    2. **Reputation Loss**: 
        - 20% for each incorrect verification.
    3. **Reputation Gain**: 
        - 5% for each correct verification.
    4. **Minimum Reputation**: 0%
    5. **Maximum Reputation**: 100%

### Reputation Rewards
Reputation rewards are given to verifiers based on their reputation score. The rewards are distributed as follows:
    - **Reputation Reward**: 100 BLUV per week for a reputation score of 90% or higher.
    - **Maximum Reward**: 100 BLUV per week.

### Reputation Penalty
1. If a verifier's reputation score falls below 50%, they will be penalized. The penalty is as follows:
    - **Penalty**: 50% of the rewards will be deducted for a reputation score below 50%.
    - **Slashing**: The verifier will be slashed if the reputation score falls below:
        a. 20%: 80% of the stake will be [slash](#verifier-slashing).
            - A top-up of 80% of the stake is required to continue as a verifier.
        b. 10%: 100% of the stake will be [slash](#verifier-slashing).
            - The verifier will be removed from the system.
2. If a verifier's reputation score falls below 90%, they will be penalized. The penalty is as follows:
    - **Penalty**: 10% of the rewards will be deducted for a reputation score below 90%.
3. If a new player is not verified within 2 hours, all assigned verifiers will be penalized. The penalty is as follows:
    - **Penalty**: 10% reputation will be deducted for each player not verified within 2 hours.
    - **Duration**: The penalty will last for the duration of the \$BLLUV cycle.
4. If a verifier is not active for more than 1 week, they will be penalized. The penalty is as follows:
    - **Penalty**: 25% of stake will be slashed for each week of inactivity.
5. If the total of [unverified players](#player-verification-distribution) exceed 15 all verifiers will be penalized. The penalty is as follows:
    - **Penalty**: 5% reputation will be deducted for each player not verified within 24 hours.

### Verifier Slashing
If a verifier is found to be dishonest or inaccurate in their verification and voting, they will be slashed of their stake. The BLUV stake will be then distributed to:
    - **Verifiers**: 80%
    - **Developers**: 10%
    - **Community**: 10%

### Player Verification Distribution
The player verification distribution is the random assignment of a new player's profile to 4 verifiers when they join the ByteLuv ecosystem. The distribution is as follows:
1. 4 out of 10 verifiers must verify the player to be considered verified.
2. At least 4 Verifiers must verify the player within 24 hours to avoid [penalties](#reputation-penalty).
3. If the criteria are not met, the player will be randomly assigned to another set of 10 verifiers.

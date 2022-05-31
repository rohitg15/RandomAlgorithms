# Spelling Checker by Peter Norvig

python implementation of a simple probabilistic spell-check by peter norvig based on http://norvig.com/spell-correct.html

## Idea

The core of Peter's idea is to use probabilities to identify which word the user would want to have typed as opposed to
what they actually typed. 

To that effect, consider 

P(c|w) - where c is the candidate word we want to consider showing to the user and w is the actual word typed

we use Baye's theorem to rewrite P(c|w) as P(c) * P(w|c) / P(w)

Thus, the best possible result that we would like to show is ** max( P(c|w) for all c in candidates(w) ) **

1. since P(w) doesn't change for each candidate, we factor that out
2. we obtain P(c) from known word lists (Recall: P(c) is the probability of the word c occuring in the language)
3. we use a hack to get P(w|c) - Recall: P(w|c) is the probability that the user would type w given that they meant c. 

The rest of the program is faily straightforward and we can implement this in less than 50 lines of python code.

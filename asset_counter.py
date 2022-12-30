from driveIX import get_model_names

model_names = get_model_names()
ethnic_tokens = set([x.split("_")[1] for x in model_names])
ethnic_counts = dict.fromkeys(ethnic_tokens, 0)
age_tokens = set([x.split("_")[0][1:] for x in model_names])
age_counts = dict.fromkeys(age_tokens, 0)
sex_tokens = set([x.split("_")[0][0] for x in model_names])
sex_counts = dict.fromkeys(sex_tokens, 0)

for model in model_names:
    for key in ethnic_counts:
        if key == model.split("_")[1]:
            ethnic_counts[key] += 1
    for key in sorted(age_counts):
        if key == model.split("_")[0][1:]:
            age_counts[key] += 1
    for key in sorted(sex_counts):
        if key == model.split("_")[0][0]:
            sex_counts[key] += 1

print(sorted(ethnic_counts.items()), len(ethnic_counts))
print(sorted(age_counts.items()), len(age_counts))
print(sorted(sex_counts.items()))

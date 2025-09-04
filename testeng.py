
from summary_reverse_pred_eng_native import simple_pred


context = "The Eiffel Tower was built in 1889 for the World's Fair."


dialogue = simple_pred(context, do_sample=True)

print("Input Context:", context)
print("Generated Dialogue:")
for line in dialogue:
    print("-", line)
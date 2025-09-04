# test_eng.py
from summary_reverse_pred_eng_native import simple_pred

# give the model some context
context = "The Eiffel Tower was built in 1889 for the World's Fair."

# generate dialogue
dialogue = simple_pred(context, do_sample=True)

print("Input Context:", context)
print("Generated Dialogue:")
for line in dialogue:
    print("-", line)
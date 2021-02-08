"""An example pf alias in meet cook"""
# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    """will the food be cooked the desired amount? Boolean"""
    alias = time * temperature * pressure * COOKED_CONSTANT
    if desired_state == 'well-done' and alias >= WELL_DONE:
        return True
    if desired_state == 'medium' and alias >= MEDIUM:
        return True
    return False

# alias = our_really_really_long_var_name
ALIAS = is_cookeding_criteria_satisfied(50, 350, 20, "well-done")
print(ALIAS)

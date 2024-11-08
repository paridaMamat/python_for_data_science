import time
from datetime import datetime

# Get the current time in seconds since the epoch (January 1, 1970)
current_time = time.time()

# Format the time in seconds since the epoch
seconds_since_epoch = f"Seconds since January 1, 1970: {current_time:.4f} or {current_time:.2e} in scientific notation"

# Get the current date in the format "Oct 21 2022"
current_date = datetime.now().strftime("%b %d %Y")

# Print the results
print(seconds_since_epoch)
print(current_date)

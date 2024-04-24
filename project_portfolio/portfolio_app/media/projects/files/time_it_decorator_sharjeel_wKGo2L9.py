import time

# Define a decorator function to measure the execution time of a function
def timeit(fx):
    def modified_add(*args, **kwargs):
        # Record the start time before executing the function
        start_time = time.time()

        # Call the original function with its arguments
        fx(*args, **kwargs)

        # Record the end time after the function has executed
        end_time = time.time()

        # Calculate the execution time
        execution_time = end_time - start_time

        # Print the execution time along with the function name
        print(f"The {fx.__name__} function took {execution_time:.9f} seconds to execute.")

    # Return the wrapper function, which now includes timing functionality
    return modified_add

# Decorate the add function with the timeit decorator
@timeit
def add(a, b):
    # Perform some operation (in this case, addition)
    c = a + b
    print('The added function result is:', c)

# Call the decorated add function with specific arguments
add(32, 56)




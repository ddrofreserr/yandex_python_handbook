def result_accumulator(f):
    results = []

    def decorated(*args, method='accumulate', **kwargs):
        nonlocal results
        
        if method == 'accumulate':
            results.append(f(*args, **kwargs))
            return None
        
        elif method == 'drop':
            results.append(f(*args, **kwargs))
            ans = results.copy()
            results.clear()
            return ans
        
    return decorated

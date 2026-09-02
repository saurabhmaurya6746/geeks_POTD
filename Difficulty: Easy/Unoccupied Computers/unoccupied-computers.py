class Solution:
    def solve(self, n, s):
        # Track currently occupied computers
        computers_in_use = 0
        # Track customers who are currently using computers
        current_customers = set()
        # Track customers who were rejected
        rejected_count = 0
    
        for event in s:
            if event not in current_customers:
                # Customer arrives
                if computers_in_use < n:
                    # Assign a computer
                    computers_in_use += 1
                    current_customers.add(event)
                else:
                    # No computer available, reject customer
                    rejected_count += 1
                    # Mark as rejected so we know to ignore their departure
                    current_customers.add(event)
                    # We need to track rejected customers separately
                    if not hasattr(self, '_rejected'):
                        self._rejected = set()
                    self._rejected.add(event)
            else:
                # Customer departs
                if event not in getattr(self, '_rejected', set()):
                    # Only free computer if they were actually using one
                    computers_in_use -= 1
                current_customers.remove(event)
    
        return rejected_count
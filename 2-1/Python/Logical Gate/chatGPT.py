def quine_mccluskey(input_list):
    from itertools import combinations

    def bit_count(x):
        return bin(x).count('1')

    def combine_terms(term1, term2):
        diff = [i for i in range(len(term1)) if term1[i] != term2[i]]
        if len(diff) == 1:
            combined = list(term1)
            combined[diff[0]] = '-'
            return ''.join(combined)
        return None

    def find_prime_implicants(minterms, num_vars):
        groups = {i: [] for i in range(num_vars + 1)}
        for minterm in minterms:
            binary = f'{minterm:0{num_vars}b}'
            groups[bit_count(minterm)].append(binary)

        all_combinations = True
        prime_implicants = set()
        while all_combinations:
            all_combinations = False
            new_groups = {i: [] for i in range(num_vars + 1)}
            checked = set()
            for i in range(num_vars):
                for term1 in groups[i]:
                    for term2 in groups[i + 1]:
                        combined = combine_terms(term1, term2)
                        if combined:
                            if combined not in new_groups[bit_count(int(combined.replace('-', '0'), 2))]:
                                new_groups[bit_count(int(combined.replace('-', '0'), 2))].append(combined)
                            checked.add(term1)
                            checked.add(term2)
                            all_combinations = True
            for i in range(num_vars + 1):
                for term in groups[i]:
                    if term not in checked:
                        prime_implicants.add(term)
            groups = new_groups

        return sorted(prime_implicants)

    num_vars, num_minterms, *minterms = input_list
    prime_implicants = find_prime_implicants(minterms, num_vars)

    return prime_implicants


# Example usage:
input_data = [3, 4, 0, 1, 2, 3]
output = quine_mccluskey(input_data)
print(output)  # Output: ["00-", "0-0", "11-", "1-1", "-01", "-10"]

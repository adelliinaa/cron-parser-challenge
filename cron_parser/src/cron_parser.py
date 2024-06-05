from typing import List


def expand_field(field: str, min_val: int, max_val: int) -> List[int]:
    if field == '*':
        return list(range(min_val, max_val + 1))
    result = []
    parts = field.split(',')
    for part in parts:
        if '-' in part:
            start, end = map(int, part.split('-'))
            if start < min_val or end > max_val:
                raise ValueError(f"Value out of range: {start}-{end} (expected between {min_val} and {max_val})")
            result.extend(range(start, end + 1))
        elif '/' in part:
            base, step = part.split('/')
            base = int(base) if base != '*' else min_val
            step = int(step)
            if base < min_val or base > max_val:
                raise ValueError(f"Base value out of range: {base} (expected between {min_val} and {max_val})")
            result.extend(range(base, max_val + 1, step))
        else:
            value = int(part)
            if value < min_val or value > max_val:
                raise ValueError(f"Value out of range: {value} (expected between {min_val} and {max_val})")
            result.append(value)
    return sorted(result)

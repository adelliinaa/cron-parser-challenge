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
            if part.startswith('*/'):
                step = int(part[2:])
                if not 1 <= step <= (max_val - min_val):
                    raise ValueError(f"Step value out of range: {step} (expected between 1 and {max_val - min_val})")
                result.extend(range(min_val, max_val + 1, step))
            else:
                raise ValueError(f"Invalid step value: {part}. Only '*' is allowed before '/'")
        else:
            value = int(part)
            if value < min_val or value > max_val:
                raise ValueError(f"Value out of range: {value} (expected between {min_val} and {max_val})")
            result.append(value)

    return sorted(result)

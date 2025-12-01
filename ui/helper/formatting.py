def milliseconds_to_time(milliseconds: int) -> str:
    seconds = milliseconds / 1000
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60

    time = [f"{hours:.0f} hour{"s" if hours > 1 else ""}" if hours > 0 else "",
            f"{minutes:.0f} minute{"s" if minutes > 1 else ""}" if minutes > 0 else "",
            f"{seconds:.0f} second{"s" if seconds > 1 else ""}"]
    time = list(filter(lambda i: i, time))
    

    return ", ".join(time)


if __name__ == "__main__":
    print(milliseconds_to_time(10000000))
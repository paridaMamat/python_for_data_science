def NULL_not_found(obj: any) -> int:
    try:
        if obj is None:
            print(f"Nothing: {obj} {type(obj)}")
        elif isinstance(obj, float) and obj != obj:
            print(f"Cheese: {obj} {type(obj)}")
        elif isinstance(obj, bool) and obj is False:
            print(f"Fake: {obj} {type(obj)}")
        elif isinstance(obj, int) and obj == 0:
            print(f"Zero : {obj} {type(obj)}")
        elif isinstance(obj, str) and obj == '':
            print(f"Empty : {obj} {type(obj)}")
        else:
            print("Type not Found")
            return 1
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
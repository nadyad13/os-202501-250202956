reference = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3

frame = []
fault = 0
hit = 0

print("LRU Page Replacement")
print("--------------------")

for page in reference:
    if page in frame:
        frame.remove(page)
        frame.append(page)
        hit += 1
        status = "Hit"
    else:
        if len(frame) < frames:
            frame.append(page)
        else:
            frame.pop(0)
            frame.append(page)
        fault += 1
        status = "Fault"

    print(f"Page {page} -> {status} | Frame: {frame}")

print("\nTotal Page Fault (LRU):", fault)
print("Total Page Hit   (LRU):", hit)

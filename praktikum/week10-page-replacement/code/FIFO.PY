# FIFO Page Replacement Algorithm

reference = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3

frame = []
fault = 0
hit = 0
index = 0  # penunjuk FIFO

print("FIFO Page Replacement")
print("---------------------")

for page in reference:
    if page in frame:
        hit += 1
        status = "Hit"
    else:
        if len(frame) < frames:
            frame.append(page)
        else:
            frame[index] = page
            index = (index + 1) % frames
        fault += 1
        status = "Fault"

    print(f"Page {page} -> {status} | Frame: {frame}")

print("\nTotal Page Fault (FIFO):", fault)
print("Total Page Hit   (FIFO):", hit)

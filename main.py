import finding_differences
import makingdata

if __name__ == "__main__":
    level = 3
    path = "images/villain.jpg"
    limit = 4
    for i in range(level):
        makingdata.processing_data(path, i + 1, limit)
        finding_differences.spotting(i + 1)

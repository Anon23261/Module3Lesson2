# Module3Lesson2
Assignment

1. Tuple Mastery
   Explanation
Enumeration: enumerate(itineraries, start=1) gives both the index (for numbering) and tuple values in the format (traveler_name, origin, destination).
String Formatting: f"Itinerary {i}: {traveler_name} - From {origin} to {destination}" formats each itinerary string with numbered headings.
Final Formatting: .strip() removes the trailing newline.

2. Python Data Structure Challenges in Real-World Scenarios
   Explanation
The add_book function takes the library list, book_title, and author as inputs.
We create a tuple for the new book and check if it's already in the list.
If it’s a new book, we add it to the library and notify the user; otherwise, we notify the user that it’s a duplicate.

3. Mastering Tuple Packing and Unpacking in Python
   Explanation
Unpacking Tuples: In the for loop, each tuple in orders is unpacked directly into customer_name, product, and quantity. This allows us to avoid indexing and makes the code more readable.

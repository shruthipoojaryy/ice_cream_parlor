//If running directly from github
step1:
git clone <repository-url>
cd ice_cream_parlor

step2:Set up a virtual environment (optional but recommended):
python -m venv env
.\env\Scripts\activate  # For Windows
source env/bin/activate  # For macOS/Linux

step3:Install dependencies:
pip install -r requirements.txt

step4:Initialize the SQLite database:
sqlite3 ice_cream_parlor.db

step5:Running the Application
Start the Flask development server:

run using 
python app.py
Access the application:
Open your web browser and go to http://127.0.0.1:5000

///////////////////////////////

//if running using docker

1) Overview

This is a fictional ice cream parlor application built with Python and Flask, using SQLite for database management. It allows managing seasonal flavors, ingredient inventory, customer suggestions, and allergies. Users can maintain a cart of favorite products, search and filter offerings, and add allergens.

2)Prerequisites
Before you begin, ensure you have the following installed:
- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Python 3.x

3) Project Structure
ice_cream_parlor/
├── __init__.py
├── app.py
├── database.py
├── models.py
├── views.py
└── templates/
    ├── index.html
    ├── search.html
    ├── filter.html
    └── cart.html


4)Setup Instructions
Clone the Repository
git clone <repository_url>
cd ice_cream_parlor

5) Install Dependencies
pip install -r requirements.txt

6)Docker Setup
Building the Docker Image
```
docker build -t ice_cream_parlor .


7) Running the Docker Container
```
docker run --rm -d -p 5000:5000 ice_cream_parlor

8)Access your application at `http://localhost:5000`.

9)Managing Docker Containers
```
# View container logs
docker logs <container_id_or_name>

# Stop and remove the container
docker stop <container_id_or_name>
docker rm <container_id_or_name>

10)Testing Steps
End-to-End Testing

1.Homepage Access:
   - Open a web browser and navigate to `http://localhost:5000`.
   - Verify that the homepage loads correctly without errors.

2. Flavor Management:
   - Navigate to the flavor management section and add a new flavor.
   - Verify that the flavor is successfully added to the database.

3. Search and Filter Functionality:
   - Use the search and filter options to find specific flavors or ingredients.
   - Verify that the search results are accurate and the filters work as expected.

4. Cart Functionality:
   - Add items to the cart and proceed to checkout.
   - Verify that the cart displays the selected items and calculates the total correctly.

5. Error Handling:
   - Intentionally trigger errors (e.g., entering invalid data) and verify that the application handles them gracefully with appropriate error messages.

11)Troubleshooting

- If you encounter issues during testing, check Docker's [documentation](https://docs.docker.com/) or inspect container logs with `docker logs`.

12) Contributing

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

13)License

This project is licensed under the [MIT License](LICENSE).
- Replace `<repository_url>`, `<container_id_or_name>`, and other placeholders with actual values applicable to your project.
- This file provides a complete guide starting from setting up the development environment to running the application in Docker, testing its functionality, troubleshooting issues, and contributing to the project.
- Customize sections and details based on your specific application requirements, such as adding more detailed setup instructions or expanding on testing scenarios.

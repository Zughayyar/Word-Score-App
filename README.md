# Word Score App

This is the Word Score App, a simple application that calculates the score of a given word based on certain rules.

This README provides an overview of how to handle real-world challenges, explains why the application is I/O bound, and outlines strategies for scaling the application in a distributed environment.

## Requirements

- [uv](https://docs.astral.sh/uv): A tool used to manage the environment for this project.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Zughayyar/Word-Score-App.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Word-Score-App
    ```

3. Install the necessary dependencies. This project uses `uv` to manage the environment:

    ```bash
    uv install
    ```

## Starting the Project

To start the project, use the following command:

```bash
uv run main.py
```

## Real World Challenges and Constraints

When developing the **Word Score App**, several real-world challenges need to be considered:

1. **Link Depth (Navigating Links):**
   - When collecting URLs or processing linked content, it’s important to determine how deep you should navigate to find additional links. Going too deep can significantly increase processing time and complexity. A balance should be struck between depth and performance, possibly introducing configurable depth limits for users to set.

2. **Error Handling - Invalid URLs:**
   - If a URL doesn't exist or returns a 404 error, the application should gracefully handle the situation by logging the error and either skipping the URL or retrying with a different approach. It's essential to provide clear feedback to users if URLs are invalid or unreachable.

3. **Error Handling - Network Issues:**
   - If a network issue occurs, such as a timeout or connectivity problem, the application should implement retry logic. This ensures that intermittent issues don't disrupt the entire process. Consider adding a retry limit or exponential backoff for retries to prevent overloading the system.

4. **Error Handling - HTML Syntax Errors:**
   - If the HTML page being processed contains syntax errors, the application should have a robust error handling mechanism in place. This could involve skipping the page, logging the issue for review, or attempting to recover by parsing the content more leniently. It’s important to ensure that errors in the HTML structure do not cause the entire process to fail.

By anticipating and addressing these challenges, the **Word Score App** can handle a wide variety of real-world scenarios while maintaining stability and performance.

## CPU Bound Analysis

The app is primarily **I/O bound**, not CPU bound. Here's why:
- The majority of time is spent on I/O operations like downloading pages, reading from disk, and network communication, which are slower than CPU operations.
- CPU usage is focused on string operations for word counting, which are relatively quick compared to I/O tasks.
- Although using `ThreadPoolExecutor` helps utilize CPU time more efficiently by parallelizing operations, the bottleneck remains I/O.

## Scaling Over Multiple Servers/Containers

- **Load Balancer:** Use tools like Nginx, HAProxy, or cloud services (AWS ELB, Google Cloud Load Balancing) to distribute tasks. Consider message queues (e.g., RabbitMQ, Apache Kafka) for task distribution.

- **Database for Storing URLs and Occurrences:** Use databases (PostgreSQL, MySQL, Redis) to track processed URLs and store results for resuming operations. Suggested schema: `url`, `word`, `occurrences`, and `processed`.

- **Microservices Architecture:**
  - Separate tasks into services: URL Collector, Page Downloader, Word Counter, and Result Aggregator.
  - **Benefits:** Scalability, maintainability, and resilience. Use REST APIs, gRPC, or message queues for communication.

This overview outlines strategies for scaling the app in a distributed environment.


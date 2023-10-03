Real-time Task Monitoring Application

Welcome to our Real-time Task Monitoring Application! This platform is designed to create long-running tasks and monitor their progress in real-time using a modern stack of technologies.
Technologies and Reasons

    Django Channels: Extends Django to handle WebSockets, which is a communication protocol that provides full-duplex communication channels over a single TCP connection. This is crucial for real-time updates.

    Celery: An asynchronous task queue/job queue based on distributed message passing. It's used for executing long-running tasks in the background, ensuring the main application continues running smoothly.

    Redis: Serves as our message broker for Celery, managing the distribution of tasks to worker nodes. It also aids in maintaining the WebSocket connections for Django Channels.

    Docker & Docker Compose: Ensures consistent environments for both development and production. By containerizing our services, we can guarantee the application runs the same regardless of where Docker is running.

    React: A powerful JavaScript library for building the frontend user interface. It facilitates the creation of interactive UIs with efficient updates and rendering.

Getting Started

    Make sure you have Docker and Docker Compose installed.
    Navigate to the project directory.
    Run docker-compose up to start the services.
    Open a browser and navigate to the frontend service URL.

License

All rights reserved. This software and associated documentation files (the "Software"), may not be used, copied, redistributed, modified, or distributed without prior written consent. Use of the Software without agreement and consent is strictly prohibited. All other use is strictly prohibited and may violate relevant federal and state laws.
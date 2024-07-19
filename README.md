# User Management Application

## Project Overview

This project is designed to manage user names and details. It includes:

- **Frontend**: Built with React.js, featuring two components:
  - A form for collecting user data.
  - A list for displaying usernames and their emails.

- **Backend**: Developed using Django with two APIs:
  - One for storing user data.
  - Another for retrieving user data.

The backend application is hosted on AWS EC2 using Docker, and the frontend application is deployed with CloudFront and S3.

## Tech Stack

- **React.js**: Frontend
- **Django**: Backend
- **SQLite3**: Database
- **AWS S3**: Storage
- **AWS CloudFront**: CDN
- **AWS EC2**: Hosting
- **Docker**: Containerization
- **Nginx**: Proxy

## Architecture

![Architecture Diagram](https://github.com/gauthamkv07/Roulettech/blob/main/architecture.jpg)

## Backend Application

1. **Docker**: Built the project and pushed the image to Docker Hub.
2. **VPC Setup**: 
   - Created a VPC with one private and one public subnet.
   - Used a NAT instance in the public subnet to provide internet access to the private subnet (instead of a NAT Gateway).
3. **Bastion Host**: Created an instance to SSH into the EC2 instance.
   - Installed Docker and hosted the application.
   - Enabled HTTP requests on the Bastion Host to access the application.
4. **Nginx**: Configured Nginx to direct traffic from the Bastion Host to port 8000 on the private EC2 instance.

**Note**: Enabling HTTP on the Bastion Host exposes it to potential security vulnerabilities. Best practices would include using a load balancer or other secure methods for accessing the application, setting up a single private subnet, using a NAT Gateway for internet access, and creating a Virtual Private Gateway for secure access.

## Frontend Application

1. **Build**: Used npm to build the project, which generated a `build` directory.
2. **S3 Deployment**: Uploaded the build files to an AWS S3 bucket and configured CORS permissions.
3. **CloudFront**: Set up a CloudFront distribution to serve content from the S3 bucket, specifying `index.html` as the default document for the entry point to the application.
4. **API Connectivity**: Used the IP address of the Bastion Host for API requests.

## Conclusion

With this setup, the full-stack application was successfully developed and deployed. It was a rewarding experience and a great opportunity to learn and create something new. I’m pleased with the outcome and thrilled to see the application fully operational.

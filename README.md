# revolut-task

In this implementation, the redis-py library is used to connect to a Redis instance. 
When a user information is saved or updated, it is stored in Redis using the set command. 
When a hello message is requested for a user, the user information is retrieved from Redis using the get command. 
If the user information exists, it is converted to a datetime object and used to generate the hello message. If the user information doesn't exist, an error message is returned.

# Commands

## To run docker image locally
docker run -p 8080:5000 -d revolut_task_image

## To push docker image to registry
docker image tag revolut_task_image registry-host:5000/myadmin/revolut_task_image:latest

## To deploy this application on kubernetes cluster

kubectl apply -f deployment.yaml


# Comments

Considering that redis cluster is created on AWS/GCP so will be supplying that as a part of appconfig. For now that is considered as localhost but for supplying DNS address docker run can with `-e` parameter to supply that as environment var.

The solution I provided is a basic example that meets the requirements of the prompt. However, the "best" solution depends on the specific needs and constraints of the system and organization deploying the application. Here are some factors that could influence the choice of solution:

    Scalability: Will the application need to handle a high volume of traffic or store a large amount of data? If so, a more robust database solution, such as a SQL or NoSQL database, may be more appropriate than Redis.
    Resilience: How critical is the application to the organization's operations? If it's essential, then a more fault-tolerant deployment architecture, such as a multi-region or multi-cloud setup, may be necessary.
    Security: What are the organization's security requirements and compliance regulations? Depending on the level of sensitivity of the data being stored, additional security measures may be necessary, such as encryption or access controls.
    Cost: How much can the organization afford to spend on infrastructure and maintenance? Depending on the budget, a simpler solution with less overhead, such as a cloud-managed database or serverless architecture, may be more cost-effective.

In summary, the best solution depends on a variety of factors and requires a thorough analysis of the organization's needs and constraints.


#No-Downtime Deployment

To deploy the application with no-downtime, we can use a rolling deployment strategy, which involves gradually updating the application instances one by one without any downtime. We can use Kubernetes or a similar container orchestration tool to manage the deployment.

Ways to achieve no-downtime deployment :

Create a Kubernetes deployment with multiple replicas of the application pods.
Configure a Kubernetes service to expose the deployment to the load balancer or ingress.
Update the Docker image in the deployment to a new version, using a rolling update strategy.
Monitor the rollout status to ensure that each pod is updated successfully before moving on to the next one.
Optionally, use canary releases or A/B testing to gradually expose the new version to a subset of users before rolling it out to everyone.


# GRAFANA INTEGRATION

ChirpStack Network Server provides a Prometheus metrics endpoint for monitoring the performance of ChirpStack services. 
Grafana supports querying Prometheus. 

For more information about : 
Grafana please visit : [https://grafana.com/]()
Prometheus please visit [https://prometheus.io/]()


##  Ports

 - grafana : 3000
 - prometheus : 9090 

## Operations

    # Launch docker-compose in chirpstack-docker
    docker-compose up 
    # now open grafana by typing http://localhost:3000 in URL emplacement or you can do it from the terminal by typing
    xdg-open http://localhost:3000 
    

##  Dashboards

Dashboard should be imported by hand into Grafana.

The files to load are into **configuration/grafana/dashboards**



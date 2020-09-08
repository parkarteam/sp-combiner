ARG PROJECT

ENV MODEL_NAME Combiner
ENV API_TYPE REST
ENV SERVICE_TYPE COMBINER
ENV PERSISTENCE 0

FROM image-registry.openshift-image-registry.svc:5000/$PROJECT/sp-lr-classifier-image:latest
RUN echo "---> copying source"
COPY . /microservice
WORKDIR /microservice




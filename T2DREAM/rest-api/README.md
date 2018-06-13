# T2DREAM Application Programming Interface (API)

The T2DREAM API provides programmatic access to T2DREAM portal and drives data query and submission functionality. The T2DREAM API uses JSON and standard HTTP verbs for communication with the portal.

There are several third-party tools that can be used with T2DREAM REST API, we have tested following tools that can be used for communicating with our portal:

| Tool          | Description          |
| ------------- |:-------------:| 
| [JSON Formatter](https://jsonformatter.org/) | Web browser plugin for Safari |
| [JSONVIEW](https://addons.mozilla.org/en-us/firefox/addon/jsonview/) | Web browser plugin for Chrome and Firefox |   
| [Restlet](https://restlet.com/) | Web browser plugin for Chrome |
| [Curl](https://curl.haxx.se/) | Command line tool |
|[Postman REST Client](https://www.getpostman.com/) | Tool for API development |

## T2DREAM Accession Ids
Every object (e.g., experiment, annotation, biosamples, antibodies, data file etc.) have unique accession TSTXXXXXXXX ids.  API request – response can be made to retrieve specific individual, group or mashup of these objects.

## Search and Retrieval Examples

### Web browser JSON pretty-printer plugin
JSON pretty-printer plugin for web browser can be used to view page as JSON.  In order to view page as JSON add “?format=json” to the URL

Example: To request metadata for experiment TSTSR112545

 http://www.t2dream-demo.org/experiments/TSTSR112545/?format=json

![pretty-printer](https://github.com/T2DREAM/rest-api/blob/master/images/JSONVIEW%20o:p.png)

### Curl

Prerequisite:  json.tool provides command line interface to validate and pretty-print JSON 

Installation for OS X and Linux:

```
$ pip install jsontool
```

Example of a request to annotation endpoint using annotation id, that retrieves annotation metadata: 

```
$ curl –L -H "Accept: application/json" http://www.t2dream-demo.org/annotations/TSTSR027410/ | python -m json.tool > 13-state_model_liver.json
```

![annotation_metadata](https://github.com/T2DREAM/rest-api/blob/master/images/annotation_metadata.png)

 Example of a request to match objects that match RRBS: 

```
curl -L -H "Accept: application/json" http://www.t2dream-demo.org/search/?searchTerm=RRBS | python -m json.tool > RRBS
```

Retrieval of all ATAC-seq experiments in TSV format:

```
curl -L "Accept: application/json" 'www.t2dream-demo.org/report.tsv?type=Experiment&searchTerm=ATAC-seq'
```

## Programmatic access to metadata 

T2DREAM_metadata_access.py script abstracts the GET request for metadata retrieval. It takes metadata type and accession id and returns metadata in JSON format.

The following metadata endpoints are available from T2DREAM API to access metadata programmatically 

|Metadata Endpoints (type) | Description|
|------------- |:-------------:| 
| experiment | Includes assay metadata, replicate information and data files |
| annotation | Metadata for an annotation set |
| files | Metadata for a data file (e.g., fastq, bigwig, bed, bam, bigBed,  tagAlign, sra) |
| biosamples |  Metadata for biosamples |
| antibodies | Metadata for antibodies |
| target | metadata for target gene |

The REST-API codebase is available on T2DREAM REST API GitHub Repository 

Prerequisite: python modules - argparse , json, requests 

Example: Download antibody metadata

```
python2 T2DREAM_metadata_access.py --accession TSTAB000404 --type antibodies
```
Truncated output

![metadata_output](https://github.com/T2DREAM/rest-api/blob/master/images/metadata_access_example_output.png)

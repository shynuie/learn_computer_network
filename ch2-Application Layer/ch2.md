# CH2. Level7: Application Layer

## I.Overview
----
### Content

* conceptual and implementation aspects of application-layer protocols
    * client-server paradigm
    * peer-to-peer paradigm (P2P)

* learn about protocols from popular application-layer protocols
    * HTTP
    * SMTP, IMAP
    * DNS

* programming network applications
    * socket API

---
### Creating a network app

* write programs that:
    * run on (different) end systems
    * communicate over network
    * e.g., web server software communicated with browser software

* no need to write software for network-core devices
    * network-core devices do not run user applications
    * applications on end systems allows for rapid app development, propagation

---
### Client-server paradigm

* Server
    * always-on host
    * permanent IP address
    * often in data centers, for scaling

* Client
    * contact, communicate with server
    * may be intermittently (間接的) connected
    * may be dynamic IP addresses
    * do not communicate directly with each other
    * e.g., HTTP, IMAP, FTP
---
### Peer-peer architecture

* no always-on server
* arbitrary end systems directly communicate
* peers request service from other peers, provide service in return to other peers;
* `self scalability`: new peers bring new service capacity, as well as new service demands.
* peers are intermittently connected and change IP addresses frequently
    * complex management

---
### Processes communicating
* process: program running within a host
    * within same host, two processes communicate using inter-process communication (defined by OS)
    * processes in different hosts communicate by exchanging messages

* clients, servers
    * client process: process that initiates communication
    * server process: process that waits to be contacted

---
### Socket

<img src="imgs/socket.png">

* process sends/receive messages to/from its socket
* socket analogous to door
    * sending process shoves message out door
    * sending process relies on transport infrastructure//基礎架構 on other side of door to deliver message to socket at receiving process
    * two sockets involved: one on each side

* to receive messages, process must have identifier
* host device has unique 32-bit IP address  
* `Does IP address of host on which process runs suffice for identifying the process?` No, many processes can be running on same host -> using port

---

### Addressing process

* Identifier includes `IP address` and `port numbers` associated with process on host. IP address for device, port for process.
* port numbers example
    * HTTP server: 80
    * mail server: 25
* to send HTTP message to gaia.cs.umass.edu web server:
    * IP address: 128.119.254.12
    * port number: 80
---

### An application-layer protocol defines

* types of message exchange
    * request, response
* message syntax//句法
    * what fields in messages & how fields are delineated//劃定
* message semantics//語義
    * meaning of information in fields
* rules for when and how process send & respond to messages

* open protocols
    * defined in (IETF) RFCs, everyone has access to protocol definition
    * allows for interoperability
    * e.g., HTTP, SMTP

* proprietary protocols
    * e.g., Skype, Line, Online game
    * provides high security for data transmit

* `What transport service does an app need?`  
    Should consider with
    * data integrity
        * Some apps (e.g., file transfer, web transactions) require 100% reliable data transfer
        * other apps (e.g., audio/video) can tolerate some loss
    * throughput
        * some apps (e.g., multimedia) require minimum amount of throughput to be 'effective'
        * other apps ('elastic apps') make use of whatever throughput they get (e.g., email)
    * timing
        * some apps (e.g., Internet telephony, interactive games) require low delay to be "effective"
    * security
        * encryption, data integrity,...

<img src="imgs/transport_service_requirements.png">

---
### Securing TCP

* Vanilla TCP & UDP sockets
    * no encryption
    * clear text passwords sent into socket traverse Internet in clear text (!)

* Transport Layer Security (TLS) 
    * provides encrypted TCP connections
    * data integrity
    * end-point authentication

<img src="imgs/tls.png">

---
### Web and HTTP
First, a quick review
* web page consists of `objects`, each of which can be on different Web servers
* object can be HTML file, JPEG image, Java applet, audio file,...
* web page consists of base `HTML-file` which includes several referenced objects, each addressable by a `URL`, e.g.,

<img src="imgs/url.png">

---
### HTTP overview

* `HTTP: Hypertext transport protocol`
    * Web's application layer protocol
    * client/server model:
        * client: browser does: 
            * requests, receives via HTTP protocol;
            * displays Web objects.
        * server: Web server sends objects in response to requests

* `HTTP uses TCP` 

    Step-by-Step
    1. Client initiates TCP connection (creates socket) to server, port 80
    2. server accepts TCP connection from client
    3. HTTP messages (application-layer protocol messages) exchanged between browser (HTTP client) and Web server (HTTP server)
    4. TCP connection closed

* `HTTPs = HTTP over TLS`
    * port 443

* `HTTP is "stateless"`
    * server maintains no information about past client requests
    ---
    ### aside  
    protocol that maintain "state" are complex!
    * past history (state) must be maintained;
    * if server/client crashes, their views of "state" may be inconsistent, must be reconciled
    ---
---
### HTTP connections: two types
* `Non-persistent HTTP`
    * pipelines
        1. TCP connection opened
        2. at most one object sent over TCP connection
        3. TCP connection closed

    * issues
        <img src = "imgs/non_persistent_http.png">  
        * RTT = Round Trip Time
        * requires 2 RTTs per object (one for building connection, one for object transport)
        * OS overhead for each TCP connection
        * browsers often open multiple parallel TCP connections to fetch referenced objects in parallel


    downloading multiple objects required multiple connections
* `Persistent HTTP` (Supported after HTTP 1.1)
    * pipelines
        1. TCP connection opened to a server
        2. multiple objects can be sent over single TCP connection between client, and that server
        3. TCP connection closed
    * issues
        * server leaves connection opened after sending response
        * subsequent HTTP messages between same client/server sent over connection
        * client sends requests as soon as it encounters a referenced object
        * as little as one RTT for all the referenced objects (cutting response time in half)
---
### HTTP request message
* two types of HTTP messages: `request`,`response`
* `HTTP request message`:
    * ASCII (human-readable format)

    <img src="imgs/request_message.png">

    <img src="imgs/request_message2.png">

    * methods
        * POST
            * web page often includes form input
            * user input sent from client to server in entity body of HTTP POST request message
        * GET
            * include user data in URL field of HTTP GET request message (following a '?')
            * e.g., www.somesite.com/animalsearch`?monkeys&banana`
        * HEAD
            * requests header (only) that would be returned if specified URL were requested with an HTTP GET method
            * usually would be utilized to check whether the content/object existing on the server
        * PUT
            * upload new file (object) to server
            * completely replaces file that exists at specified URL with content in entity body of POST HTTP request message
    
* `HTTP response message`:

    <img src = "imgs/response_message.png">

    * HTTP response status codes
        * status code appears in 1st line in server-to-client response message.
        * 200 OK
            * request succeeded, requested object later in this message
        * 301 Moved permanently
            * requested object moved, new location specified later in this message (in Location:field)
        * 400 Bad Request
            * request msg not understood by server
        * 404 Not Found
            * requested document not fount on this server
        * 505 HTTP Version Not Supported

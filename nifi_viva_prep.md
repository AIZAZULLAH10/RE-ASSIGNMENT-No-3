# Viva Preparation: Apache NiFi Data Flow

This document explains the Apache NiFi part of your assignment and provides a quick way to run it and grab screenshots for your submission.

## What is Apache NiFi?
Apache NiFi is a powerful data routing and transformation tool. In reverse engineering, it helps us visually map and monitor how data moves in and out of a legacy system (e.g., from old CSV files into a new modern database) without having to read thousands of lines of legacy code.

## Quickest Setup Using Docker (Recommended)
Instead of installing Java and downloading the NiFi zip manually, you can run it via Docker in one command.

1. Open your terminal in this folder.
2. Run this command to start Apache NiFi:
   ```bash
   docker run --name nifi -p 8080:8080 -d apache/nifi:latest
   ```
3. Wait about 1-2 minutes for NiFi to fully start up.
4. Open your web browser and go to: `http://localhost:8080/nifi`

## Building the Flow for Screenshots

Once the NiFi UI is open, you need to create a flow to show in your assignment screenshots.

### Step 1: Add Processors (The building blocks)
Drag the **Processor** icon (looks like a square tag in the top toolbar) onto the empty grid/canvas. Do this 4 times and search for the following processors:
1. `GetFile` (Simulates reading data from the legacy system)
2. `SplitText` (Splits the data into rows)
3. `LogAttribute` (Logs the data so you can analyze it)
4. `PutDatabaseRecord` (Simulates pushing to a new modern system)

### Step 2: Connect Them
Hover over a processor, a green arrow will appear. Drag that arrow to the next processor to connect them.
* Connect `GetFile` -> `SplitText`
* Connect `SplitText` -> `LogAttribute`
* Connect `LogAttribute` -> `PutDatabaseRecord`

### Step 3: Take the Screenshot
Take a screenshot of the connected flow on the canvas. This is your primary screenshot for the NiFi requirement!

## Answering Viva Questions on NiFi
**Q: Why use NiFi for reverse engineering?**
A: Legacy systems often have complex, undocumented data flows. NiFi allows us to tap into legacy data sources (files, databases, APIs), visually map the data movement, and analyze its structure using a drag-and-drop interface instead of manually tracing through old code.

**Q: What is a Processor?**
A: A processor is a functional block in NiFi that does one specific job, like reading a file (`GetFile`), filtering data, or writing to a database (`PutDatabaseRecord`).

**Q: How does this help modernize a system?**
A: By connecting `GetFile` (legacy source) to `PutDatabaseRecord` (modern destination), we can continuously migrate data from the old system to a new system in real-time, side-by-side.

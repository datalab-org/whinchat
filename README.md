# <div align="center"><i>whinchat</i></div>

<div align="center">
<a href="https://github.com/datalab-org/whinchat/releases"><img src="https://badgen.net/github/release/datalab-org/whinchat?icon=github&color=blue"></a>
<a href="https://github.com/datalab-org/whinchat"><img src="https://badgen.net/github/license/datalab-org/whinchat?icon=license&color=purple"></a>
<a href="https://datalab-org.github.io/whinchat"><img src="https://github.com/datalab-org/whinchat/actions/workflows/docs.yml/badge.svg"></a>
</div>

Whinchat is a [*datalab*](https://datalab-org.io) plugin generated using the [datalab-app-plugin-template](https://github.com/datalab-org/datalab-app-plugin-template) template.

Whinchat was previously a core data block until version v0.7.x of *datalab*, when it was moved out to this repository.
The initial version at the time of moving was released as v1.0.0; likely v2.0.0 will follow soon with a restructuring of the plugin to use more modern agent runners and tools.


<!-- This file was edited with the assistance of an AI model and requires human review from the contributor. -->
The plugin provides the server-side `ChatBlock` (blocktype `chat`) and its webapp component, declared in the manifest at `src/whinchat/webapp/index.js` and collected into the *datalab* webapp by `invoke dev.install`.
The npm packages used by `MessageBubble.vue` (`markdown-it`, `highlight.js` and `mermaid`) must be provided by the core *datalab* webapp, as plugins cannot yet declare their own npm dependencies.

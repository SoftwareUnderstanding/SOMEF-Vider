# Home

**Author:** Vitoriox

Main view of the page. It contains the majority of the components,
and it is responsible for communicating the different components 
with each other and with the service.

```html
<home/> 
<!-- The HTML is handled by the Vue Router plugin -->
```
## Data

| Name                | Type      | Initial value                                               | Description                                                                                                  |
|---------------------|-----------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| `metadata`          | `Object`  | `{}`                                                        | Stores the metadata obtained from de SOMEF service, this data will be passed to the MetadataCard component   |
| `showLoadingDialog` | `Boolean` | `False`                                                     | Flag that hides/shows the LoadingDialog component                                                            |
| `showMetadataCard`  | `Boolean` | `False`                                                     | Flag that hides/shows the MetadataCard component                                                             |
| `showErrorDialog`   | `Boolean` | `False`                                                     | Flag that hides/shows the ServerResponseDialog component                                                     |
| `serverResponse`    | `Object`  | `Null`                                                      | Stores the response obtained from the server, this data will be passed to the ServerResponseDialog component |
| `formData`          | `Object`  | {`url`: null,`threshold`: null,`ignoreClassifiers`: false,} | Stores the user input of the SomefForm component. Is used to call the SOMEF service.                         |

## Methods

### submitForm()

Executed when the event `submit` of the SomefForm component is caught.
Stores the form information, shows de loading dialog and calls 
`fetchMetadata()` with de form data.

**Syntax**

```typescript
submitForm(url, threshold, ignoreClassifiers): void
```

### fetchMetadata()

This method only function is to use de AxiosService function `getMetadata` to call 
the SOMEF service and fetch the metadata. 
If the response is OK, stores the metadata, hides the loading dialog and shows the
metadata card. Otherwise, shows the server error response.

**Syntax**

```typescript
submitForm(url, threshold, ignoreClassifiers): void
```

### downloadMetadata()

This method requires that the metadata is fetched before calling because the method
behaviour is to tell the service that the user wants to download the metadata in
a file.

Uses the AxiosService function `downloadMetadata`. If the response is OK, the navigator
will download de file in the computer. Otherwise, shows the server error response.

**Syntax**

```typescript
downloadMetadata(fileType):void
```


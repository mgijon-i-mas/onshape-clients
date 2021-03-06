/**
 * Onshape REST API
 * The Onshape REST API consumed by all clients.
 *
 * OpenAPI spec version: 1.93
 * Contact: api-support@onshape.zendesk.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export class BTThumbnailSizeInfo {
    'size'?: string;
    'sheetName'?: string;
    'mediaType'?: string;
    'href'?: string;
    'uniqueId'?: string;
    'viewOrientation'?: string;
    'renderMode'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "size",
            "baseName": "size",
            "type": "string"
        },
        {
            "name": "sheetName",
            "baseName": "sheetName",
            "type": "string"
        },
        {
            "name": "mediaType",
            "baseName": "mediaType",
            "type": "string"
        },
        {
            "name": "href",
            "baseName": "href",
            "type": "string"
        },
        {
            "name": "uniqueId",
            "baseName": "uniqueId",
            "type": "string"
        },
        {
            "name": "viewOrientation",
            "baseName": "viewOrientation",
            "type": "string"
        },
        {
            "name": "renderMode",
            "baseName": "renderMode",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return BTThumbnailSizeInfo.attributeTypeMap;
    }
}


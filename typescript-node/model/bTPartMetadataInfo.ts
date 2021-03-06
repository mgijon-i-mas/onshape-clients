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

import { BTCustomPropertyDefinitionInfo } from './bTCustomPropertyDefinitionInfo';
import { BTPartAppearanceInfo } from './bTPartAppearanceInfo';
import { BTPartMaterialInfo } from './bTPartMaterialInfo';
import { BTThumbnailInfo } from './bTThumbnailInfo';

export class BTPartMetadataInfo {
    'name'?: string;
    'id'?: string;
    'state'?: BTPartMetadataInfo.StateEnum;
    'description'?: string;
    'revision'?: string;
    'microversionId'?: string;
    'customProperties'?: { [key: string]: string; };
    'vendor'?: string;
    'productLine'?: string;
    'title1'?: string;
    'title2'?: string;
    'title3'?: string;
    'partQuery'?: string;
    'partId'?: string;
    'unflattenedPartId'?: string;
    'configurationId'?: string;
    'href'?: string;
    'thumbnailInfo'?: BTThumbnailInfo;
    'elementId'?: string;
    'project'?: string;
    'material'?: BTPartMaterialInfo;
    'partNumber'?: string;
    'bodyType'?: string;
    'isMesh'?: boolean;
    'thumbnailConfigurationId'?: string;
    'isFlattenedBody'?: boolean;
    'referencingConfiguredPartNodeIds'?: Array<string>;
    'appearance'?: BTPartAppearanceInfo;
    'customPropertyDefinitions'?: { [key: string]: BTCustomPropertyDefinitionInfo; };
    'isHidden'?: boolean;
    'ordinal'?: number;
    'propertySourceTypes'?: { [key: string]: number; };

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "state",
            "baseName": "state",
            "type": "BTPartMetadataInfo.StateEnum"
        },
        {
            "name": "description",
            "baseName": "description",
            "type": "string"
        },
        {
            "name": "revision",
            "baseName": "revision",
            "type": "string"
        },
        {
            "name": "microversionId",
            "baseName": "microversionId",
            "type": "string"
        },
        {
            "name": "customProperties",
            "baseName": "customProperties",
            "type": "{ [key: string]: string; }"
        },
        {
            "name": "vendor",
            "baseName": "vendor",
            "type": "string"
        },
        {
            "name": "productLine",
            "baseName": "productLine",
            "type": "string"
        },
        {
            "name": "title1",
            "baseName": "title1",
            "type": "string"
        },
        {
            "name": "title2",
            "baseName": "title2",
            "type": "string"
        },
        {
            "name": "title3",
            "baseName": "title3",
            "type": "string"
        },
        {
            "name": "partQuery",
            "baseName": "partQuery",
            "type": "string"
        },
        {
            "name": "partId",
            "baseName": "partId",
            "type": "string"
        },
        {
            "name": "unflattenedPartId",
            "baseName": "unflattenedPartId",
            "type": "string"
        },
        {
            "name": "configurationId",
            "baseName": "configurationId",
            "type": "string"
        },
        {
            "name": "href",
            "baseName": "href",
            "type": "string"
        },
        {
            "name": "thumbnailInfo",
            "baseName": "thumbnailInfo",
            "type": "BTThumbnailInfo"
        },
        {
            "name": "elementId",
            "baseName": "elementId",
            "type": "string"
        },
        {
            "name": "project",
            "baseName": "project",
            "type": "string"
        },
        {
            "name": "material",
            "baseName": "material",
            "type": "BTPartMaterialInfo"
        },
        {
            "name": "partNumber",
            "baseName": "partNumber",
            "type": "string"
        },
        {
            "name": "bodyType",
            "baseName": "bodyType",
            "type": "string"
        },
        {
            "name": "isMesh",
            "baseName": "isMesh",
            "type": "boolean"
        },
        {
            "name": "thumbnailConfigurationId",
            "baseName": "thumbnailConfigurationId",
            "type": "string"
        },
        {
            "name": "isFlattenedBody",
            "baseName": "isFlattenedBody",
            "type": "boolean"
        },
        {
            "name": "referencingConfiguredPartNodeIds",
            "baseName": "referencingConfiguredPartNodeIds",
            "type": "Array<string>"
        },
        {
            "name": "appearance",
            "baseName": "appearance",
            "type": "BTPartAppearanceInfo"
        },
        {
            "name": "customPropertyDefinitions",
            "baseName": "customPropertyDefinitions",
            "type": "{ [key: string]: BTCustomPropertyDefinitionInfo; }"
        },
        {
            "name": "isHidden",
            "baseName": "isHidden",
            "type": "boolean"
        },
        {
            "name": "ordinal",
            "baseName": "ordinal",
            "type": "number"
        },
        {
            "name": "propertySourceTypes",
            "baseName": "propertySourceTypes",
            "type": "{ [key: string]: number; }"
        }    ];

    static getAttributeTypeMap() {
        return BTPartMetadataInfo.attributeTypeMap;
    }
}

export namespace BTPartMetadataInfo {
    export enum StateEnum {
        INPROGRESS = <any> 'IN_PROGRESS',
        PENDING = <any> 'PENDING',
        RELEASED = <any> 'RELEASED',
        OBSOLETE = <any> 'OBSOLETE',
        REJECTED = <any> 'REJECTED',
        DISCARDED = <any> 'DISCARDED'
    }
}

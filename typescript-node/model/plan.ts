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


export class Plan {
    'id'?: string;
    'object'?: string;
    'amount'?: number;
    'created'?: number;
    'currency'?: string;
    'interval'?: string;
    'intervalCount'?: number;
    'livemode'?: boolean;
    'metadata'?: { [key: string]: string; };
    'name'?: string;
    'statementDescriptor'?: string;
    'trialPeriodDays'?: number;
    'statementDescription'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "object",
            "baseName": "object",
            "type": "string"
        },
        {
            "name": "amount",
            "baseName": "amount",
            "type": "number"
        },
        {
            "name": "created",
            "baseName": "created",
            "type": "number"
        },
        {
            "name": "currency",
            "baseName": "currency",
            "type": "string"
        },
        {
            "name": "interval",
            "baseName": "interval",
            "type": "string"
        },
        {
            "name": "intervalCount",
            "baseName": "intervalCount",
            "type": "number"
        },
        {
            "name": "livemode",
            "baseName": "livemode",
            "type": "boolean"
        },
        {
            "name": "metadata",
            "baseName": "metadata",
            "type": "{ [key: string]: string; }"
        },
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "statementDescriptor",
            "baseName": "statementDescriptor",
            "type": "string"
        },
        {
            "name": "trialPeriodDays",
            "baseName": "trialPeriodDays",
            "type": "number"
        },
        {
            "name": "statementDescription",
            "baseName": "statementDescription",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return Plan.attributeTypeMap;
    }
}


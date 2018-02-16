// DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.
package types

import (
	"gopkg.in/validator.v2"
)

type Group struct {
	Addr   string   `json:"addr,omitempty"`
	Alias  []string `json:"alias" validate:"nonzero"`
	KeyPub []string `json:"keyPub,omitempty"`
	Owners int32    `json:"owners" validate:"nonzero"`
	Uid    int32    `json:"uid" validate:"nonzero"`
}

func (s Group) Validate() error {

	return validator.Validate(s)
}

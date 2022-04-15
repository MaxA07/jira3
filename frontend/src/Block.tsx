import React, { useState } from 'react';

interface IBlockParams {
    value: number;
}

export const Block: React.FC<IBlockParams> = ({ value }) => {
    const [name, setName] = useState(true);

    const handleClick = () => {
        setName(false)
    }

    return (
     <div onClick={handleClick}>
        {value}
     </div>
    )
}

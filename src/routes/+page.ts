import type { PageLoad } from './$types';
import type { Crossword } from '../@types';
import { env } from '$env/dynamic/public';

import { gql, request } from 'graphql-request';

export const load: PageLoad = async () => {
    const data = await request<{ crosswords: Crossword[] }>(env.PUBLIC_HYGRAPH_API_URL as string, gql`
        {
            crosswords(orderBy: date_DESC) {
                slug
                title
                author {
                    name
                }
                semester
                date
                width
                height
                data
            }
        }
    `);

	return {
        crosswords: data.crosswords,
	};
}
